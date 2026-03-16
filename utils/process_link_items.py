import os
import re
import json
from copy import deepcopy


# =========================================
# 正则定义
# =========================================

ROMAN_RE = r"M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})"
ARABIC_RE = r"\d+"
NUM_RE = rf"(?:{ARABIC_RE}|{ROMAN_RE})"

# Figure / Table 引用
FIGURE_REF_RE = re.compile(
    rf"(?i)\bfig(?:ure)?s?\.?\s*({NUM_RE})(?:\s*[\(\[]?([a-z])[\)\]]?)?\b"
)
TABLE_REF_RE = re.compile(
    rf"(?i)\btab(?:le)?s?\.?\s*({NUM_RE})(?:\s*[\(\[]?([a-z])[\)\]]?)?\b"
)

# 整块公式
FORMULA_FULL_RE = re.compile(r"^\s*\$\$[\s\S]+?\$\$\s*$")

# 子图
SUBFIG_ONLY_RE = re.compile(r"^\s*\(?[A-Za-z]\)\s*[:.\-–—]?\s*$")
SUBFIG_PREFIX_RE = re.compile(r"^\s*\(?([A-Za-z])\)\s*[:.\-–—]?\s*")

# 文本衔接
LOWER_START_RE = re.compile(r"^\s*[a-zα-ω0-9]")
SENT_END_RE = re.compile(r"[.!?。！？;；]\s*$")
FORMULA_PREV_END_RE = re.compile(r"[:：,，]\s*$")


# =========================================
# 工具函数
# =========================================

def ensure_list(x):
    if x is None:
        return []
    if isinstance(x, list):
        return x
    return [x]


def normalize_space(text: str) -> str:
    if text is None:
        return ""
    return text.replace("\u00A0", " ").strip()


def merge_text(a: str, b: str) -> str:
    a = a or ""
    b = b or ""
    if not a:
        return b
    if not b:
        return a
    if a.endswith("-"):
        return a + b.lstrip()
    if a.endswith((" ", "\n")) or b.startswith((" ", "\n")):
        return a + b
    return a + " " + b


def merge_linked_items(items_a, items_b):
    """
    合并两个 linked_items 列表，去重。
    去重依据：(type, label) 相同则认为是同一项，保留第一个出现的。
    """
    if not items_a:
        return items_b or []
    if not items_b:
        return items_a or []
    
    merged = list(items_a)
    seen = {(item["type"], item["label"]) for item in items_a}
    
    for item in items_b:
        key = (item["type"], item["label"])
        if key not in seen:
            merged.append(item)
            seen.add(key)
    
    return merged


def dedup_list(seq):
    out = []
    seen = set()
    for x in seq:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def filter_existing_image_sources(image_sources):
    """
    - 保留 http/https 等远程资源
    - 对本地路径：若文件不存在则丢弃
    """
    kept = []
    for src in ensure_list(image_sources):
        if src == "./text_resources/A_MEMS_Resonant_Accelerometer_With_High_Performance_of_Temperature_Based_on_Electrostatic_Spring_Softening_and_Continuous_Ring-Down_Technique/vlm/images/0c8f62a78f8fa29ebe580ba91069f58b204a23f85ebd16c266ff67cc4042dd0b.jpg":
            continue

        if src is None:
            continue
        if not isinstance(src, str):
            # 非字符串的 source，先原样保留，避免误删上游结构化对象
            kept.append(src)
            continue
        s = src.strip()
        if not s:
            continue
        if re.match(r"(?i)^https?://", s):
            kept.append(s)
            continue
        # 本地路径（绝对/相对），不存在则过滤
        if os.path.exists(s):
            kept.append(s)
            continue
    return dedup_list(kept)


def roman_to_int(s: str):
    if not s:
        return None
    s = s.upper()
    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev = 0
    for ch in reversed(s):
        if ch not in roman_map:
            return None
        val = roman_map[ch]
        if val < prev:
            total -= val
        else:
            total += val
            prev = val
    return total


def normalize_num(num: str) -> str:
    num = (num or "").strip()
    if not num:
        return ""
    if re.fullmatch(r"\d+", num):
        return str(int(num))
    if re.fullmatch(rf"(?i){ROMAN_RE}", num):
        val = roman_to_int(num)
        if val is not None:
            return str(val)
    return num.upper()


def extract_refs(text: str, kind: str):
    text = text or ""
    regex = FIGURE_REF_RE if kind == "Figure" else TABLE_REF_RE
    refs = []
    for m in regex.finditer(text):
        num = normalize_num(m.group(1))
        sub = (m.group(2) or "").lower()
        refs.append({
            "kind": kind,
            "num": num,
            "sub": sub,
            "label": f"{kind} {num}{sub}" if sub else f"{kind} {num}"
        })
    return refs


def has_image(entry: dict) -> bool:
    return "image_source" in entry and entry["image_source"] not in (None, "", [])


def is_formula(entry: dict) -> bool:
    """
    判断是否为公式：
    1. 优先检查内容是否包含 $$
    2. 其次检查是否有图片
    """
    text = normalize_space(entry.get("content", ""))
    # 优先认为包含 $$ 的是公式
    if "$$" in text:
        return True
    if not has_image(entry):
        return False
    return bool(FORMULA_FULL_RE.fullmatch(text))


def is_table_caption(entry: dict) -> bool:
    if not has_image(entry):
        return False
    text = normalize_space(entry.get("content", ""))
    return bool(TABLE_REF_RE.search(text))


def is_figure_like(entry: dict) -> bool:
    if not has_image(entry):
        return False
    text = normalize_space(entry.get("content", ""))
    if FIGURE_REF_RE.search(text):
        return True
    if text == "" or SUBFIG_ONLY_RE.fullmatch(text) or SUBFIG_PREFIX_RE.match(text):
        return True
    return False


def should_merge_text(prev_item, next_item):
    if prev_item["kind"] != "text" or next_item["kind"] != "text":
        return False

    prev_text = normalize_space(prev_item.get("content", ""))
    next_text = normalize_space(next_item.get("content", ""))

    if not prev_text or not next_text:
        return False

    if (not SENT_END_RE.search(prev_text)) and LOWER_START_RE.search(next_text):
        return True

    return False


# =========================================
# 第一步：基础归一化
# =========================================

def entry_type(entry: dict) -> str:
    if is_formula(entry):
        return "formula"
    if is_table_caption(entry):
        return "table"
    if is_figure_like(entry):
        return "figure_like"
    return "text"


def normalize_entries(contents):
    items = []
    for i, c in enumerate(contents):
        # 如果是 text 类型但有 image_source，则跳过（删除）
        block_type = entry_type(c)
        if block_type == "text" and c.get("image_source"):
            continue
        
        item = {
            "orig_index": i,
            "id": c.get("id", f"doc_{i}"),
            "content": c.get("content", "") or ""
        }
        if "image_source" in c:
            item["image_source"] = ensure_list(c.get("image_source"))
        
        # 如果是公式，删除 image_source
        if block_type == "formula":
            item.pop("image_source", None)
        
        item["block_type"] = block_type
        items.append(item)
    return items


# =========================================
# 第二步：合并 Figure / 子图块
# 注意：不删除图表本身，只把连续子图合并成一个 figure 条目
# =========================================

def is_real_figure_caption(entry: dict) -> bool:
    if not has_image(entry):
        return False
    text = normalize_space(entry.get("content", ""))
    return bool(FIGURE_REF_RE.search(text))

def is_subfigure_block(entry: dict) -> bool:
    if not has_image(entry):
        return False
    text = normalize_space(entry.get("content", ""))
    if text == "":
        return True
    if SUBFIG_ONLY_RE.fullmatch(text):
        return True
    if SUBFIG_PREFIX_RE.match(text) and not FIGURE_REF_RE.search(text):
        return True
    return False

def extract_figure_number(text: str):
    """
    从文本中提取 Figure 编号（如 "Figure 1"）
    返回 (num, sub) 或 (None, None)
    """
    text = normalize_space(text)
    m = FIGURE_REF_RE.search(text)
    if m:
        num = normalize_num(m.group(1))
        sub = (m.group(2) or "").lower()
        return (num, sub)
    return (None, None)


def is_empty_or_subfig_only(text: str) -> bool:
    """
    判断是否为空或仅包含子图标记（如 "a)", "(a)", "A)", "(A)" 等）
    """
    text = normalize_space(text)
    if text == "":
        return True
    if SUBFIG_ONLY_RE.fullmatch(text):
        return True
    return False


def collect_blocks(items):
    """
    改进的子图吸收规则：
    
    1. formula 单独保留
    2. table 单独保留
    3. 真正的 Figure caption 作为锚点
       - 只向上吸收满足条件的**连续**子图块
       - 子图条件：
         a) 子图的caption为空或仅包含子图标记（如"a)"、"(a)"等）
         b) 或者子图的caption包含相同的Figure编号（如"Fig. 1(a)"、"(a) Fig. 1"等）
         c) 关键：子图必须是连续的，中间不能有其他类型的块（text/formula等）
    4. 单独出现、且后面没有caption可归属的子图块，移除（不保留为残缺figure）
    """

    blocks = []
    pending_subfigs = []   # 暂存尚未归属的子图块
    absorbed_subfig_indices = set()  # 记录已被吸收的子图索引

    for item in items:
        cur = deepcopy(item)

        if cur["block_type"] == "formula":
            cur["kind"] = "formula"
            cur["merged_from"] = [cur["orig_index"]]
            blocks.append(cur)
            # 遇到 formula，清空待吸收的子图（因为不连续了）
            pending_subfigs = []
            continue

        if cur["block_type"] == "table":
            cur["kind"] = "table"
            cur["labels"] = extract_refs(cur["content"], "Table")
            cur["merged_from"] = [cur["orig_index"]]
            blocks.append(cur)
            # 遇到 table，清空待吸收的子图（因为不连续了）
            pending_subfigs = []
            continue

        # 真正的 Figure caption：作为 anchor
        if is_real_figure_caption(cur):
            # 提取当前主图注的 Figure 编号
            main_fig_num, _ = extract_figure_number(cur["content"])

            group = {
                "orig_index": cur["orig_index"],
                "id": cur["id"],
                "content": cur["content"],
                "image_source": ensure_list(cur.get("image_source")),
                "kind": "figure",
                "labels": extract_refs(cur["content"], "Figure"),
                "merged_from": [cur["orig_index"]],
            }

            # 只向上吸收满足条件的连续子图块
            if pending_subfigs:
                valid_subfigs = []

                for p in pending_subfigs:
                    # 检查子图是否已被其他主图注吸收
                    if p["orig_index"] in absorbed_subfig_indices:
                        continue

                    subfig_text = normalize_space(p.get("content", ""))
                    subfig_fig_num, _ = extract_figure_number(subfig_text)

                    # 子图的caption为空或仅包含子图标记
                    if is_empty_or_subfig_only(subfig_text):
                        valid_subfigs.append(p)
                    # 或者子图的caption包含相同的Figure编号
                    elif subfig_fig_num is not None and subfig_fig_num == main_fig_num:
                        valid_subfigs.append(p)
                    else:
                        # 不符合条件的子图，停止向上吸收
                        break

                # 吸收有效的子图
                if valid_subfigs:
                    merged_content_parts = []
                    merged_images = []
                    merged_from = []

                    for p in valid_subfigs:
                        merged_content_parts.append(p.get("content", ""))
                        merged_images.extend(ensure_list(p.get("image_source")))
                        merged_from.extend(p.get("merged_from", [p["orig_index"]]))
                        absorbed_subfig_indices.add(p["orig_index"])

                    # 子图内容放前面，主图注放后面
                    merged_content_parts.append(group["content"])
                    merged_images.extend(group["image_source"])
                    merged_from.extend(group["merged_from"])

                    group["content"] = " ".join(
                        [x for x in merged_content_parts if x is not None and str(x).strip() != ""]
                    )
                    group["image_source"] = dedup_list(merged_images)
                    group["merged_from"] = merged_from

                    # 从pending_subfigs中移除已吸收的子图
                    pending_subfigs = [p for p in pending_subfigs if p["orig_index"] not in absorbed_subfig_indices]

            blocks.append(group)
            # 清空待吸收的子图
            pending_subfigs = []
            continue

        # 子图块：只暂存，等待后面最近的主图注来向上吸收
        if is_subfigure_block(cur):
            cur["kind"] = "figure"
            cur["labels"] = []
            cur["merged_from"] = [cur["orig_index"]]
            pending_subfigs.append(cur)
            continue

        # 普通文本
        cur["kind"] = "text"
        cur["merged_from"] = [cur["orig_index"]]
        blocks.append(cur)
        # 遇到 text，清空待吸收的子图（因为不连续了）
        pending_subfigs = []

    # 扫描结束后，未被吸收的子图块移除（不保留为残缺figure）
    # pending_subfigs 中剩余的都是未被吸收的子图，直接丢弃

    return blocks



# =========================================
# 第三步：合并误切分的普通文本
# =========================================

def merge_broken_text_blocks(blocks, allow_cross_kinds=("figure", "table")):
    """
    合并被错误切分的 text。
    允许跨过中间的 figure/table，把后面的 text 接到前面的 text。
    中间跨过的图表块保留原位，不删除。
    
    例如:
      text(A) -> figure -> figure -> text(b...)
    若 A 不是正常句末，且 b... 小写开头，则把 text(b...) 合并到 text(A)。
    """

    if not blocks:
        return blocks

    blocks = [deepcopy(b) for b in blocks]
    removed = set()

    i = 0
    n = len(blocks)

    while i < n:
        if i in removed:
            i += 1
            continue

        cur = blocks[i]
        if cur["kind"] != "text" and  cur["kind"] != "formula":
            i += 1
            continue

        cur_text = normalize_space(cur.get("content", ""))
        if not cur_text:
            i += 1
            continue

        # 当前已经是完整句末，就不尝试向后拼
        if SENT_END_RE.search(cur_text):
            i += 1
            continue

        # 向后找最近的 text，中间允许跨过 figure/table
        j = i + 1
        crossed_only_allowed = True

        while j < n:
            if j in removed:
                j += 1
                continue

            nxt = blocks[j]

            if nxt["kind"] == "text" or nxt["kind"] == "formula":
                break

            if nxt["kind"] in allow_cross_kinds:
                j += 1
                continue

            # 遇到 formula 或其他块，停止跨越
            crossed_only_allowed = False
            break

        if not crossed_only_allowed or j >= n:
            i += 1
            continue

        nxt = blocks[j]
        nxt_text = normalize_space(nxt.get("content", ""))

        if not nxt_text:
            i += 1
            continue

        # 关键条件：后一段小写开头
        if LOWER_START_RE.search(nxt_text):
            blocks[i]["content"] = merge_text(blocks[i]["content"], blocks[j]["content"])
            blocks[i]["merged_from"] = blocks[i].get("merged_from", []) + blocks[j].get("merged_from", [])
            
            # 合并 linked_items（去重）
            if blocks[j].get("linked_items"):
                items_a = blocks[i].get("linked_items", [])
                items_b = blocks[j].get("linked_items", [])
                blocks[i]["linked_items"] = merge_linked_items(items_a, items_b)
            
            removed.add(j)

            # 不推进 i，继续尝试把更后面的误切分 text 也吸收进来
            continue

        i += 1

    # 输出时去掉被吸收的 text
    new_blocks = []
    for idx, b in enumerate(blocks):
        if idx in removed:
            continue
        new_blocks.append(b)

    return new_blocks



# =========================================
# 第四步：把 公式 + 相邻上下文 真正合并成一个块
# 关键：吸收前后文本时，不保留原文本重复输出
# 但不删除图表、表格、其他公式本身
# =========================================

def merge_formula_with_context(blocks):
    merged = []
    i = 0
    n = len(blocks)

    while i < n:
        cur = deepcopy(blocks[i])

        if cur["kind"] != "formula":
            merged.append(cur)
            i += 1
            continue

        parts = []
        merged_from = list(cur.get("merged_from", []))
        formula_images = ensure_list(cur.get("image_source"))

        # 吸收左侧 text
        if merged:
            prev = merged[-1]
            prev_text = normalize_space(prev.get("content", ""))
            if prev["kind"] == "text" and FORMULA_PREV_END_RE.search(prev_text):
                parts.append(prev["content"])
                merged_from = prev.get("merged_from", []) + merged_from
                merged.pop()  # 关键：删除被吸收的左侧 text，避免重复

        # 当前公式
        parts.append(cur["content"])

        # 吸收右侧 text
        consumed_right = False
        if i + 1 < n:
            nxt = blocks[i + 1]
            nxt_text = normalize_space(nxt.get("content", ""))
            if nxt["kind"] == "text" and LOWER_START_RE.search(nxt_text):
                parts.append(nxt["content"])
                merged_from.extend(nxt.get("merged_from", []))
                consumed_right = True

        new_block = {
            "id": cur["id"],
            "orig_index": min(merged_from) if merged_from else cur.get("orig_index", i),
            "kind": "formula",
            "content": " ".join([p for p in parts if p and p.strip()]),
            "image_source": dedup_list(formula_images),
            "merged_from": merged_from,
        }

        merged.append(new_block)

        if consumed_right:
            i += 2
        else:
            i += 1

    return merged


# =========================================
# 第五步：建立 Figure / Table caption 索引
# 不删除图表本身行
# =========================================

def build_caption_index(blocks):
    caption_index = {}

    for idx, b in enumerate(blocks):
        if b["kind"] not in ("figure", "table"):
            continue

        std_kind = "Figure" if b["kind"] == "figure" else "Table"
        labels = b.get("labels", [])

        if not labels:
            continue

        for lb in labels:
            if lb["kind"] != std_kind:
                continue

            key = (std_kind, lb["num"])

            if key not in caption_index:
                caption_index[key] = {
                    "caption": b.get("content", ""),
                    "image_source": ensure_list(b.get("image_source")),
                    "labels": labels,
                    "block_index": idx,
                }
            else:
                caption_index[key]["caption"] = merge_text(
                    caption_index[key]["caption"],
                    b.get("content", "")
                )
                caption_index[key]["image_source"].extend(
                    ensure_list(b.get("image_source"))
                )

    # 过滤不存在的 image_source；若 Figure 没有任何有效图片，则移除该索引项
    to_delete = []
    for key, info in caption_index.items():
        kind, _num = key
        info["image_source"] = filter_existing_image_sources(info.get("image_source"))
        if kind == "Figure" and not info["image_source"]:
            to_delete.append(key)

    for key in to_delete:
        caption_index.pop(key, None)

    return caption_index


# =========================================
# 第六步：正文 / 公式 挂接 Figure/Table 引用
# 注意：不要把 linked_items 的 image_source 再复制到顶层 image_source
# =========================================

def attach_references(blocks, caption_index, local_window=None):
    caption_positions = {}
    for idx, b in enumerate(blocks):
        if b["kind"] not in ("figure", "table"):
            continue
        std_kind = "Figure" if b["kind"] == "figure" else "Table"
        for lb in b.get("labels", []):
            if lb["kind"] == std_kind:
                caption_positions.setdefault((std_kind, lb["num"]), []).append(idx)

    new_blocks = []

    for idx, b in enumerate(blocks):
        cur = deepcopy(b)

        if cur["kind"] not in ("text", "formula"):
            new_blocks.append(cur)
            continue

        text = cur.get("content", "")
        refs = extract_refs(text, "Figure") + extract_refs(text, "Table")

        linked_items = []
        seen_link = set()

        for ref in refs:
            key = (ref["kind"], ref["num"])
            if key not in caption_index:
                continue

            if local_window is not None:
                pos_list = caption_positions.get(key, [])
                if pos_list and min(abs(idx - p) for p in pos_list) > local_window:
                    continue

            if key in seen_link:
                continue
            seen_link.add(key)

            cap_info = caption_index[key]
            linked_items.append({
                "type": ref["kind"].lower(),
                "label": f"{ref['kind']} {ref['num']}",
                "caption": cap_info["caption"],
                "image_source": cap_info["image_source"]
            })

        if linked_items:
            cur["linked_items"] = linked_items

        new_blocks.append(cur)

    return new_blocks


# =========================================
# 第七步：重新输出
# 不删除公式、图表本身的行
# 正文引用图表时，不复制到顶层 image_source
# figure / table / formula 自身如果有 image_source，保留
# =========================================

def export_all_blocks(blocks):
    """
    导出所有块，同时：
    1. 逐个检查 image_source 中的 URL，删除不存在的文件
    2. 如果 image_source 为空，删除整个 doc（figure/table）或删除 linked_items（text/formula）
    """
    result = []

    for b in blocks:
        item = {
            "id": "",
            "content": b.get("content", ""),
            "block_type": b.get("kind", "text")
        }

        # 处理 image_source：逐个检查 URL 是否存在
        if b.get("image_source"):
            valid_images = filter_existing_image_sources(b.get("image_source"))
            if valid_images:
                item["image_source"] = valid_images
            elif item["block_type"] in ("figure", "table"):
                # 如果是 figure/table 且没有有效图片，则跳过整个 doc
                continue

        # 处理 linked_items：逐个检查其中的 image_source
        if b.get("linked_items"):
            valid_linked_items = []
            for linked_item in b.get("linked_items", []):
                # 检查 linked_item 中的 image_source
                if linked_item.get("image_source"):
                    valid_images = filter_existing_image_sources(linked_item.get("image_source"))
                    if valid_images:
                        linked_item = dict(linked_item)
                        linked_item["image_source"] = valid_images
                        valid_linked_items.append(linked_item)
                else:
                    valid_linked_items.append(linked_item)
            
            # 只有当有有效的 linked_items 时才保留
            if valid_linked_items:
                item["linked_items"] = valid_linked_items

        result.append(item)

    # 重新编号
    for i, item in enumerate(result):
        item["id"] = f"doc_{i}"

    return result


# =========================================
# 单文件处理
# =========================================

def process_one_file(input_file, output_file, local_window_for_ref=None):
    with open(input_file, "r", encoding="utf-8") as fr:
        contents = json.load(fr)

    # 1. 基础归一化
    items = normalize_entries(contents)

    # 2. 收集 block，合并连续子图
    blocks = collect_blocks(items)

    # 3. 合并误切分文本
    blocks = merge_broken_text_blocks(blocks)

    # 5. 建立图表索引
    caption_index = build_caption_index(blocks)

    # 6. 给正文 / 公式挂接引用
    blocks = attach_references(
        blocks,
        caption_index,
        local_window=local_window_for_ref
    )

    # 7. 导出全部 block
    result = export_all_blocks(blocks)

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as fw:
        json.dump(result, fw, ensure_ascii=False, indent=2)


# =========================================
# 批处理入口
# =========================================

if __name__ == "__main__":
    input_path = "./processed_resources/processed_3/"
    output_path = "./processed_resources/processed_4/"

    os.makedirs(output_path, exist_ok=True)

    for file_name in os.listdir(input_path)[3:4]:
        if not (file_name.endswith(".json") or file_name.endswith(".jsonl")):
            continue

        input_file = os.path.join(input_path, file_name)
        output_file = os.path.join(output_path, file_name)

        try:
            # None 表示全局匹配引用
            # 若只想查上下 3 段，可改成 3
            process_one_file(
                input_file=input_file,
                output_file=output_file,
                local_window_for_ref=None
            )
            print(f"处理完成: {file_name}")
        except Exception as e:
            print(f"处理失败: {file_name} | {e}")

    print(f"{len(os.listdir(input_path))}个文件处理完成!")
