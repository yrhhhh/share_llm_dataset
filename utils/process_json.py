import json  
import base64
import re  
from typing import List, Dict, Any  
import os

def process_content_list_v2(input_file: str, output_file: str, exclude_types: List[str] = None):  
    """  
    处理 content_list_v2.json 文件，过滤指定类型并按段落整合内容  
      
    Args:  
        input_file: 输入文件路径  
        output_file: 输出文件路径  
        exclude_types: 需要排除的类型列表  
    """  
    if exclude_types is None:  
        # 默认排除页眉页脚等不需要的内容  
        exclude_types = [  
            'page_header', 'page_footer', 'page_number',   
            'page_aside_text', 'page_footnote'  
        ]  
      
    with open(input_file, 'r', encoding='utf-8') as f:  
        data = json.load(f)  
      
    # content_list_v2.json 是按页面分组的数组  
    all_content = []  
    doc_id = 0  
    hold = []
    image_path = os.path.split(input_file)[0]
    for page_content in data:  
        if not isinstance(page_content, list):  
            continue  
              
        for block in page_content:  
            block_type = block.get('type', '')  
              
            # 跳过需要排除的类型  
            if block_type in exclude_types:  
                continue  
              
            # 提取内容  
            content = extract_content_from_block(block)  
            if content == False:
                source = block.get('content', {}).get('image_source', [])["path"]
                hold.append(os.path.join(image_path,source))
            elif block_type in ['image','table','equation_interline']:
                source = block.get('content', {}).get('image_source', [])["path"]
                hold.append(os.path.join(image_path,source))
                for h in hold :
                    if content.strip(): 
                        all_content.append({  
                            'id': f'doc_{doc_id}', 
                            'type': block_type,
                            'content': content.strip(),
                            'image_source': h
                        })  
                        doc_id += 1  
                hold = []
            else:
                hold = []
                if content.strip(): 
                    all_content.append({  
                        'id': f'doc_{doc_id}',  
                        'type': block_type,
                        'content': content.strip()
                    })  
                    doc_id += 1  
      
    # LLM 清洗
    new_contents,anal = llm_aided_content_filter(all_content,5,output_file)
    name = os.path.splitext(file)[-2]
    with open(output_file, 'w', encoding='utf-8') as f:  
        json.dump(new_contents, f, ensure_ascii=False, indent=2)  
    with open(os.path.join("/data/rhyang/download/mems_LLM/log/",f"{name}.txt"),"w") as f:
        json.dump(anal, f, ensure_ascii=False, indent=2)  
    
    print(f"处理完成{name}，共生成 {len(new_contents)} 个文档块")  
  
def extract_content_from_block(block: Dict[str, Any]) -> str:  
    """  
    从不同类型的块中提取文本内容  
    """  
    block_type = block.get('type', '')  
    content_data = block.get('content', {})  
      
    if block_type == 'paragraph':  
        # 段落类型 - 合并所有 span 内容  
        paragraph_content = content_data.get('paragraph_content', [])  
        return merge_spans_to_text(paragraph_content)  
      
    elif block_type == 'title':  
        # 标题类型  
        title_content = content_data.get('title_content', [])  
        level = content_data.get('level', 1)  
        text = merge_spans_to_text(title_content)  
        return f"{'#' * level} {text}"  
      
    elif block_type == 'image':  
        # 图片类型 - 提取图注  
        captions = content_data.get('image_caption', [])  
        caption_text = merge_spans_to_text(captions)  
        return f"{caption_text}" if caption_text else False  
      
    elif block_type == 'table':  
        # 表格类型 - 提取表注  
        captions = content_data.get('table_caption', [])  
        caption_text = merge_spans_to_text(captions)  
        return f"{caption_text}" if caption_text else False
      
    elif block_type == 'equation_interline':  
        # 公式类型  
        math_content = content_data.get('math_content', '')  
        return f"$$\n{math_content}\n$$"  
      
    elif block_type == 'code':  
        # 代码类型  
        code_content = content_data.get('code_content', [])  
        code_text = merge_spans_to_text(code_content)  
        lang = content_data.get('code_language', 'text')  
        return f"```{lang}\n{code_text}\n```"  
      
    elif block_type == 'algorithm':  
        # 算法类型  
        algo_content = content_data.get('algorithm_content', [])  
        algo_text = merge_spans_to_text(algo_content)  
        return f"```algorithm\n{algo_text}\n```"  
      
    elif block_type == 'list':  
        # 列表类型  
        list_items = content_data.get('list_items', [])  
        list_text = '\n'.join([f"- {merge_spans_to_text(item.get('item_content', []))}"   
                              for item in list_items])  
        return list_text  
      
    else:  
        # 其他类型，尝试提取通用内容  
        for key in content_data:  
            if key.endswith('_content'):  
                content_list = content_data[key]  
                if isinstance(content_list, list):  
                    return merge_spans_to_text(content_list)  
                elif isinstance(content_list, str):  
                    return content_list  
      
    return ""  
  
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
    "model": "qwen-plus",

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

def llm_aided_content_filter(content, batch_size=10,out_file = None):
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
            "You are an academic text content cleaning assistant.\n"

            "Your task is to determine, for each paragraph or text segment, whether it **should be retained** for a literature dataset related to **MEMS (Micro-Electro-Mechanical Systems)** technology.\n"

            "### What “should be retained” means\n"

            "A text **should be retained** if it satisfies **any** of the following conditions:\n"

            "* It describes **MEMS devices, structures, materials, fabrication processes, operating principles, performance metrics, or applications**.\n"
            "* It contains **background information, methods, experimental setups, process flows, manufacturing steps, or summaries** that are relevant to MEMS research or engineering.\n"
            "* It includes **formulas, parameter explanations, experimental descriptions, or experimental results** related to MEMS.\n"
            "* It is a **figure caption** related to MEMS (even if the text is short), as long as it explains a device, structure, or technical aspect.\n"
            "* It provides **technical explanations, definitions, methods, or conclusions** associated with MEMS.\n"

            "### When to output false (i.e., “should not be retained”)\n"

            "Only output **false** in the following situations:\n"

            "* The text contains **only** author information, affiliations, funding statements, acknowledgements, or reference numbers.\n"
            "* The text is a **title or section heading** with **no real technical content**.\n"
            "* The text is something like **“[Image]”, “see figure”, “as shown below”** and does **not** include any actual technical description.\n"
            "* The text is **generic, empty, or unrelated to MEMS** and contains no meaningful technical information.\n"
            "* The text is bibliographic reference entry.\n"

            "### Important notes\n"

            "* **Do not** judge a text as false just because it is short.\n"
            "* The output must be valid JSON that can be parsed by json.loads().\n"
            "* If there is **any MEMS-related technical information**, you should output **true**.\n"
            "* When in doubt, **prefer to keep** the text rather than discard it. It is better to retain potentially valuable content than to miss it.\n"

            "### Required analysis procedure\n"

            "Before making the final decision, analyze the text according to the following steps:\n"

            "1. Determine **what the content is about** and whether it fits into one of the “should be retained” or “should not be retained” categories described above.\n"
            "2. According to the categories, analyze the content if it's a useful knowledge about MEMS and the experiment.\n"
            "3. estimate the correlation of the content with MEMS or the experiment and the probability that this text should be retained.\n"

            "### Output format requirements\n"

            "* Output **only one JSON array**.\n"
            "* The array length must be **exactly the same as the input list**.Output items id must be in the same order as the input items id.Produce exactly one output object per input item. Do not merge, split, reorder, or drop any item.\n"
            "* Each element of the array must be reshaped as {'id': <int>, 'analyze': <string>, 'correlation': <float>, 'probability': <float>},the string of the analyze should be include in double quotes, and make sure there is no other double quotes inside, if there is replace them by ' \n"
            "* the correlation and probability between 0 and 1\n"

            "### Input\n"

            "A list of text segments to be evaluated.\n\n"
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
            if results[i]['probability']<0.3:
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
            if batch_contents[i]["type"] in ['image','table','equation_interline']:
                if batch_contents[i]["content"] != []:
                    
                    new_content.append({  
                        'id': f'doc_{doc_id}',  
                        'content': batch_contents[i]["content"],
                        "image_source":batch_contents[i]["image_source"]
                    })  
                    doc_id += 1 

            elif flag[i]:
                new_content.append({  
                    'id': f'doc_{doc_id}',  
                    'content': batch_contents[i]["content"]
                })  
                doc_id += 1 
        for i in range(len(results)):
            anal.append({
                'id': f'doc_{ex_id}',  
                'type': batch_contents[i]["type"],
                'content': batch_contents[i]["content"],
                'analysis': results[i]["analyze"],
                'probability':results[i]['probability']
            })
            ex_id += 1
                    # 保存结果   


    return new_content,anal


# 使用示例  
if __name__ == "__main__":  
    file_path = "/data/rhyang/download/mems_LLM/pdf_resources/" 
    input_path = "/data/rhyang/download/mems_LLM/text_resources/"  
    output_path = "/data/rhyang/download/mems_LLM/processed_resources/processed_3/"
    model = "vlm"  
      
    # 可以自定义需要排除的类型  
    exclude_types = [  
        'page_header',   
        'page_footer',   
        'page_number',  
        'page_aside_text',  
        'page_footnote'  ,
        'title'
    ]  
    
    for file in os.listdir(file_path)[19:]:
        name = os.path.splitext(file)[0]
        input_file = os.path.join(input_path,name,model,f"{name}_content_list_v2.json")
        out_file =  os.path.join(output_path,f"{name}.json")
        process_content_list_v2(input_file, out_file, exclude_types)
        
