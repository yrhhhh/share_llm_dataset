import json

# 输入文件路径
input_file = "/data/rhyang/download/mems_LLM/text_resources/processed_1/Comi_2016_J._Micromech._Microeng._26_035006.json"  
# 输出文件路径
output_file = "/data/rhyang/download/mems_LLM/text_resources/processed_2/Comi_2016_J._Micromech._Microeng._26_035006.json"  

# 读取输入文件
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# 处理数据
result = []
for idx, item in enumerate(data):
    new_item = {
        "id": f"doc_{idx}",  # 生成 id，从 JYQ_0 开始
        "content": item["content"]  # 保留 content 字段
    }
    result.append(new_item)

# 将结果写入输出文件
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

print(f"处理完成，结果已保存到 {output_file}")