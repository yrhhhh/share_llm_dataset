import json
import re
from typing import List, Dict, Any
import os

try:
    # 在项目根目录执行时
    from utils.process_link_items import (
        normalize_entries,
        collect_blocks,
        merge_broken_text_blocks,
        merge_formula_with_context,
        build_caption_index,
        attach_references,
        export_all_blocks,
        filter_existing_image_sources,
    )
except ImportError:
    # 直接在 utils/ 目录下执行时
    from process_link_items import (  # type: ignore
        normalize_entries,
        collect_blocks,
        merge_broken_text_blocks,
        merge_formula_with_context,
        build_caption_index,
        attach_references,
        export_all_blocks,
        filter_existing_image_sources,
    )


def _pre_llm_cleanup_and_link(all_content: List[Dict[str, Any]]):
    """
    在 LLM 清洗前完成：
    - 合并误切分普通文本
    - 校验 image_source 文件是否存在；若 figure/table 无有效图片则删除该 caption 块
    - 基于 caption 建索引并给正文/公式挂接 linked_items
    """
    # 1) 归一化为 blocks
    items = normalize_entries(all_content)
    blocks = collect_blocks(items)

    # 2) 合并误切分文本
    blocks = merge_broken_text_blocks(blocks)

    # 3) 公式与上下文合并（保持与现有 pipeline 一致）
    blocks = merge_formula_with_context(blocks)

    # 4) 校验 image_source；若图/表没有任何有效图片，则去掉该 caption 块
    kept_blocks = []
    for b in blocks:
        if b.get("kind") in ("figure", "table"):
            imgs = filter_existing_image_sources(b.get("image_source"))
            if not imgs:
                # 删除 caption 本身，也就自然不会被引用挂接
                continue
            b = dict(b)
            b["image_source"] = imgs
        kept_blocks.append(b)
    blocks = kept_blocks

    # 5) 建索引 + 挂接引用
    caption_index = build_caption_index(blocks)
    blocks = attach_references(blocks, caption_index, local_window=None)

    # 6) 导出回 json 结构（含 linked_items / image_source）
    return export_all_blocks(blocks)

def estimate_token_count(text: str) -> int:
    """
    粗略估计 token 数：
    - 英文按单词/数字/符号切分
    - 中文按单字计
    如安装了 tiktoken，则优先用 tiktoken
    """
    if not text:
        return 0

    try:
        import tiktoken
        enc = tiktoken.get_encoding("cl100k_base")
        return len(enc.encode(text))
    except Exception:
        # fallback：中文单字 + 英文/数字单词 + 标点
        pattern = r'[\u4e00-\u9fff]|[a-zA-Z0-9_]+|[^\s]'
        return len(re.findall(pattern, text))


def is_text_only_block(block_info: Dict[str, Any]) -> bool:
    """
    纯文本块定义：
    - paragraph / code / algorithm / list / title / equation_interline
    - 且没有 images
    - image / table 单独成 doc
    """
    block_type = block_info.get("block_type", "")
    has_images = bool(block_info.get("images"))

    if has_images:
        return False

    return block_type in {"paragraph", "code", "algorithm", "list", "title", "equation_interline"}


def flush_doc(doc_buffer: Dict[str, Any], all_content: List[Dict[str, Any]], doc_id: int) -> int:
    """
    把当前缓存 doc 写入 all_content
    """
    text = doc_buffer.get("content", "").strip()
    images = doc_buffer.get("image_source", [])
    linked_items = doc_buffer.get("linked_items", [])

    if not text and not images:
        return doc_id

    item = {
        "id": f"doc_{doc_id}",
        "content": text,
    }
    if images:
        item["image_source"] = images
    if linked_items:
        item["linked_items"] = linked_items

    all_content.append(item)
    return doc_id + 1

def _merge_text_and_formula(blocks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    合并文本和公式块（同一章节，token < 800）
    
    规则：
    1. 图/表单独成 doc
    2. 同一章节的连续文本/公式块合并
    3. 合并后 token 不超过 800
    """
    all_content = []
    doc_id = 0
    current_doc = {
        "content": "",
        "image_source": [],
        "linked_items": [],
        "section": None,
    }

    for block in blocks:
        block_type = block.get("block_type", "")
        text = block.get("content", "").strip()
        images = block.get("image_source", [])
        section = block.get("section")

        # 图/表单独成 doc
        if block_type in ("image", "table"):
            # 先落盘当前 doc
            if current_doc["content"].strip() or current_doc["image_source"]:
                item = {
                    "id": f"doc_{doc_id}",
                    "content": current_doc["content"].strip(),
                }
                if current_doc["image_source"]:
                    item["image_source"] = current_doc["image_source"]
                if current_doc["linked_items"]:
                    item["linked_items"] = current_doc["linked_items"]
                all_content.append(item)
                doc_id += 1
                current_doc = {
                    "content": "",
                    "image_source": [],
                    "linked_items": [],
                    "section": None,
                }

            # 图/表单独成 doc
            single_item = {
                "id": f"doc_{doc_id}",
                "content": text,
            }
            if images:
                single_item["image_source"] = images
            all_content.append(single_item)
            doc_id += 1
            continue

        # 文本/公式块：尝试合并
        candidate_text = (current_doc["content"] + ("\n" if current_doc["content"] and text else "") + text).strip()
        candidate_tokens = estimate_token_count(candidate_text)

        # 检查是否需要切分：不同章节或 token 超过 800
        if current_doc["section"] is not None and current_doc["section"] != section:
            # 不同章节，先落盘当前 doc
            if current_doc["content"].strip():
                item = {
                    "id": f"doc_{doc_id}",
                    "content": current_doc["content"].strip(),
                }
                if current_doc["image_source"]:
                    item["image_source"] = current_doc["image_source"]
                if current_doc["linked_items"]:
                    item["linked_items"] = current_doc["linked_items"]
                all_content.append(item)
                doc_id += 1
            current_doc = {
                "content": text,
                "image_source": images,
                "linked_items": [],
                "section": section,
            }
        elif current_doc["content"].strip() and candidate_tokens > 800:
            # token 超过 800，先落盘当前 doc
            item = {
                "id": f"doc_{doc_id}",
                "content": current_doc["content"].strip(),
            }
            if current_doc["image_source"]:
                item["image_source"] = current_doc["image_source"]
            if current_doc["linked_items"]:
                item["linked_items"] = current_doc["linked_items"]
            all_content.append(item)
            doc_id += 1
            current_doc = {
                "content": text,
                "image_source": images,
                "linked_items": [],
                "section": section,
            }
        else:
            # 合并到当前 doc
            if not current_doc["content"].strip():
                current_doc["content"] = text
                current_doc["section"] = section
            else:
                if text:
                    current_doc["content"] += "\n" + text
            if images:
                current_doc["image_source"].extend(images)

    # 收尾
    if current_doc["content"].strip():
        item = {
            "id": f"doc_{doc_id}",
            "content": current_doc["content"].strip(),
        }
        if current_doc["image_source"]:
            item["image_source"] = current_doc["image_source"]
        if current_doc["linked_items"]:
            item["linked_items"] = current_doc["linked_items"]
        all_content.append(item)

    return all_content

def process_content_list_v2(input_file: str, name: str, exclude_types: List[str] = None):
    """
    处理 content_list_v2.json 文件，过滤指定类型并按章节/段落整合内容

    规则：
    1. 先提取所有块（不合并）
    2. LLM 清洗（过滤无用内容）
    3. 再合并文本和公式（同一章节，token < 800）
    4. 图/表单独成 doc
    5. 图表合并和链接
    """
    if exclude_types is None:
        exclude_types = [
            'page_header', 'page_footer', 'page_number',
            'page_aside_text', 'page_footnote'
        ]

    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 第一步：提取所有块（不合并）
    all_blocks = []
    current_section = None
    
    for page_content in data:
        if not isinstance(page_content, list):
            continue

        for block in page_content:
            block_type = block.get('type', '')

            # 先跳过无关块
            if block_type in exclude_types:
                continue

            content = extract_content_from_block(block, os.path.split(input_file)[0])
            text = content.get("text", "").strip()
            images = content.get("images", [])

            # 空块直接跳过
            if not text and not images:
                continue

            # 记录章节标题
            if block_type == "title":
                current_section = text
                continue

            # 每个块单独保存（包含章节信息）
            block_item = {
                "id": f"doc_{len(all_blocks)}",
                "content": text,
                "block_type": block_type,
                "section": current_section,
            }
            if images:
                block_item["image_source"] = images
            all_blocks.append(block_item)

    # 第二步：LLM 清洗
    all_blocks, anal = llm_aided_content_filter(all_blocks, 5)

    # 第三步：合并文本和公式（同一章节，token < 800）
    all_content = _merge_text_and_formula(all_blocks)

    # 第四步：图表合并和链接
    all_content = _pre_llm_cleanup_and_link(all_content)

    output_file = os.path.join(output_path, f"{name}.json")

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_content, f, ensure_ascii=False, indent=2)

    print(f"save in {output_file}")

    # 如需保存 LLM 分析日志
    with open("./log.txt", "w", encoding="utf-8") as f:
        json.dump(anal, f, ensure_ascii=False, indent=2)
  
def extract_content_from_block(block: Dict[str, Any], name) -> Dict[str, Any]:
    """
    从不同类型的块中提取文本内容
    返回:
    {
        "text": str,
        "images": List[str],
        "block_type": str,
        "is_text_only": bool
    }
    """
    block_type = block.get('type', '')
    content_data = block.get('content', {})

    result = {
        "text": "",
        "images": [],
        "block_type": block_type,
        "is_text_only": False,
    }

    if block_type == 'title':
        title_content = content_data.get('title_content', [])
        text = merge_spans_to_text(title_content).strip()
        result["text"] = text
        result["is_text_only"] = True

    elif block_type == 'paragraph':
        paragraph_content = content_data.get('paragraph_content', [])
        text = merge_spans_to_text(paragraph_content).strip()
        result["text"] = text
        result["is_text_only"] = True

    elif block_type == 'image':
        captions = content_data.get('image_caption', [])
        source_info = content_data.get('image_source', '')
        source = source_info.get("path", "") if isinstance(source_info, dict) else ""
        caption_text = merge_spans_to_text(captions).strip()
        result["text"] = f"{caption_text}." if caption_text else ""
        if source:
            result["images"] = [f"{name}/{source}"]

    elif block_type == 'table':
        captions = content_data.get('table_caption', [])
        source_info = content_data.get('image_source', '')
        source = source_info.get("path", "") if isinstance(source_info, dict) else ""
        caption_text = merge_spans_to_text(captions).strip()
        result["text"] = f"{caption_text}." if caption_text else ""
        if source:
            result["images"] = [f"{name}/{source}"]

    elif block_type == 'equation_interline':
        math_content = content_data.get('math_content', '').strip()
        source_info = content_data.get('image_source', '')
        source = source_info.get("path", "") if isinstance(source_info, dict) else ""
        result["text"] = f"$$\n{math_content}\n$$" if math_content else ""
        result["is_text_only"] = True  # 公式作为可合并的文本块
        if source:
            result["images"] = [f"{name}/{source}"]

    elif block_type == 'code':
        code_content = content_data.get('code_content', [])
        code_text = merge_spans_to_text(code_content).strip()
        lang = content_data.get('code_language', 'text')
        result["text"] = f"```{lang}\n{code_text}\n```" if code_text else ""
        result["is_text_only"] = True

    elif block_type == 'algorithm':
        algo_content = content_data.get('algorithm_content', [])
        algo_text = merge_spans_to_text(algo_content).strip()
        result["text"] = f"```algorithm\n{algo_text}\n```" if algo_text else ""
        result["is_text_only"] = True

    elif block_type == 'list':
        list_items = content_data.get('list_items', [])
        list_text = '\n'.join(
            [f"- {merge_spans_to_text(item.get('item_content', [])).strip()}"
             for item in list_items]
        ).strip()
        result["text"] = list_text
        result["is_text_only"] = True

    else:
        for key in content_data:
            if key.endswith('_content'):
                content_list = content_data[key]
                if isinstance(content_list, list):
                    result["text"] = merge_spans_to_text(content_list).strip()
                elif isinstance(content_list, str):
                    result["text"] = content_list.strip()
                break

    return result

  
def merge_spans_to_text(spans: List[Dict[str, Any]]) -> str:  
    """  
    将 span 数组合并为文本  
    """  
    if not spans:  
        return ""  
      
    text_parts = []  
    for span in spans:  
        if isinstance(span, dict):  
            content = span.get('content', '')  
        elif isinstance(span, str):  
            content = span  
        else:  
            continue  
          
        if content:  
            text_parts.append(content)  
      
    return ' '.join(text_parts)  


from openai import OpenAI
LLM_CONTENT_FILTER_CONFIG = {
    # 是否启用 LLM 内容清洗
    "enable": True,

    # OpenAI / 兼容 OpenAI 协议的服务
    "api_key": "sk-611f561606894fe4bf44f31e21906203",
    "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",

    # 使用的模型
    "model": "qwen-max",

    # 批处理相关
    "batch_size": 10,

    # 生成参数（可选，方便后续扩展）
    "temperature": 0,
    "timeout": 30,

    # 过滤策略描述（给 prompt 用，可选）
    "filter_policy": (
        "保留包含以下内容的文本："
        "核心观点、研究结论、数据、定义、步骤、方法、技术细节；"
        "过滤页眉页脚、目录、版权声明、重复描述、空泛说明。"
    )
}

def llm_aided_content_filter(content, batch_size=10):
    """使用LLM批量过滤无用内容（就地修改 pdf_info）"""
    config = LLM_CONTENT_FILTER_CONFIG
    client = OpenAI(api_key=config["api_key"], base_url=config["base_url"])
    model = config["model"]

    def evaluate_batch(contents):
        """
        输入: List[str]
        输出: List[bool] 与 contents 等长
        """
        # 让模型严格输出 JSON 数组，便于解析与对齐
        prompt = (
            "You are an academic text cleaning assistant.\n"

            "Your task is to determine whether each paragraph should be retained for a literature dataset about **MEMS (Micro-Electro-Mechanical Systems)**.\n"

            "==============================\n"
            "PRIORITY RULE\n"
            "==============================\n"
            "If the paragraph is an **author biography or CV-style description or references list**, it must be classified as **low correlation**, even if MEMS appears in the research interests.\n"

            "==============================\n"
            "WHEN TO RETAIN \n"
            "==============================\n"
            "Retain the text if it contains **technical MEMS-related information**, such as:\n"
            "* MEMS devices, sensors, actuators, or systems\n"
            "* structures, materials, fabrication processes, packaging\n"
            "* operating principles, modeling, simulations\n"
            "* experimental setups, measurements, results\n"
            "* MEMS applications (e.g., inertial sensors, biosensors, RF MEMS)\n"
            "* equations, parameters, or technical explanations\n"
            "* figure captions explaining MEMS devices or experiments\n"

            "==============================\n"
            "WHEN TO OUTPUT LOW CORRELATION\n"
            "==============================\n"
            "Output false if the text contains only non-technical metadata, such as:\n"
            "* author biography or profile\n"
            "* education history, employment history\n"
            "* research interests of an author\n"
            "* affiliations or contact information\n"
            "* acknowledgements or funding statements\n"
            "* bibliographic references or reference list\n"
            "* section titles without technical content\n"
            "* placeholders like '[Image]' or 'see figure'\n"
            "* generic or unrelated text\n"

            "Typical author biography patterns include:\n"
            "'was born in', 'received the Ph.D.', 'is currently a professor', 'his research interests include'.\n"

            "==============================\n"
            "ANALYSIS PROCEDURE\n"
            "==============================\n"
            "1. Determine **what the content is about** and whether it fits into one of the “should be retained” or “should not be retained” categories described above.\n" 
            "2. According to the categories, analyze the content if it's a useful knowledge about MEMS and the experiment.\n" 
            "3. estimate the correlation of the content with MEMS or the experiment\n"

            "==============================\n"
            "OUTPUT FORMAT\n"
            "==============================\n"
            "The output must be valid JSON that can be parsed by json.loads().\n"
            "The array length must be exactly the same as the input list and items must stay in the same order.\n"

            "Each element must follow this structure:\n"
            "{\n"
            "  'id': <string>,\n"
            "  'analyze': <string>,\n"
            "  'correlation': <float>,\n"
            "  'probability': <float>\n"
            "}\n"

            "Rules:\n"
            "* analyze must be enclosed in double quotes\n"
            "* analyze must not contain internal double quotes (replace them with ')\n"
            "* avoid to repeat content in analyze\n"
            "* correlation must be between 0 and 1\n"
            "* The output must **not** contain any Markdown or code block formatting (such as ` ```json ` and ` ``` `).\n"

            "==============================\n"
            "INPUT\n"
            "==============================\n"
            "A list of text segments to evaluate.\n\n"
            )

        for i in range(len(contents)):
            c = contents[i]["content"]
            id = contents[i]["id"]
            prompt += f"{id}. {c}\n\n"

        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        raw = resp.choices[0].message.content.strip()

        # 尽量稳健地解析 JSON（必要时做简单兜底）
        import json
        results = json.loads(raw)
        flags = [True for _ in contents]
        for i in range(len(contents)):
            if results[i]['correlation']<0.3:
                flags[i] = False          
        return [flags,results[:len(contents)]]

    doc_id = 0
    ex_id = 0
    new_content = []
    anal = []
    for start in range(0, len(content), batch_size):
        batch_contents = content[start:start + batch_size]
        eval = evaluate_batch(batch_contents) 
        flag = eval[0]# List[bool]
        results = eval[1]
        for i in range(len(batch_contents)):
            if not flag[i] and "image_source" not in batch_contents[i]:
                continue

            # 保留原条目的结构信息（image_source / linked_items / block_type 等）
            item = dict(batch_contents[i])
            item["id"] = f"doc_{doc_id}"
            new_content.append(item)
            doc_id += 1
        for i in range(len(results)):
            anal.append({
                'id': f'doc_{ex_id}',  
                'content': batch_contents[i].get("content", ""),
                'analysis': results[i]["analyze"],
                'correlation':results[i]['correlation']
            })
            ex_id += 1
                    # 保存结果   


    return new_content, anal


file_path = "./pdf_resources/" 
input_path = "./text_resources/"  
output_path = "./processed_resources/processed_3/"
# 使用示例  
if __name__ == "__main__":  
    model = "vlm"  
      
    # 可以自定义需要排除的类型  
    exclude_types = [  
        'page_header',   
        'page_footer',   
        'page_number',  
        'page_aside_text',  
        'page_footnote'  
    ]  
    
    for file in os.listdir(file_path)[0:1]:
        name = os.path.splitext(file)[0]
        input_file = os.path.join(input_path,name,model,f"{name}_content_list_v2.json")
        out_file =  os.path.join(output_path,f"{name}.jsonl")
        process_content_list_v2(input_file, name, exclude_types)
    
    print(f"process {len(os.listdir(file_path))} files")

        
