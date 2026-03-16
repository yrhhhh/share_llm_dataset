import base64
from openai import OpenAI
from utils.mulprompts import prompt_generate_qa_en
client = OpenAI(
            api_key="sk-611f561606894fe4bf44f31e21906203", # 替换为您的ZCHAT API密钥
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
        )
image_path1 = "/data/rhyang/download/mems_LLM/text_resources/Ding_2016_J._Micromech._Microeng._26_015011/vlm/images/5a822cbf97b47c0dcc349ac9d1f6f3dd764a74bbe6c8a0353b1f53f0185d6d73.jpg"
image_path2 = "/data/rhyang/download/mems_LLM/text_resources/Ding_2016_J._Micromech._Microeng._26_015011/vlm/images/475b36d6ca5a438555ae562de36c40f62e6dd0903a7640c84f2031da67bdbadb.jpg"
image_path3 = "/data/rhyang/download/mems_LLM/text_resources/Ding_2016_J._Micromech._Microeng._26_015011/vlm/images/81ebee1783a652f2a0a27ec1283959de3322ced7be2abdd65ed53c69a117c2db.jpg"


with open(image_path1, "rb") as f:
    image1_base64 = base64.b64encode(f.read()).decode("utf-8")

with open(image_path2, "rb") as f:
    image2_base64 = base64.b64encode(f.read()).decode("utf-8")

with open(image_path3, "rb") as f:
    image3_base64 = base64.b64encode(f.read()).decode("utf-8")


data_url1 = f"data:image/jpeg;base64,{image1_base64}"
data_url2 = f"data:image/jpeg;base64,{image2_base64}"
data_url3 = f"data:image/jpeg;base64,{image3_base64}"

resp = client.chat.completions.create(
    model="qwen3.5-397b-a17b",   # 按你的实际模型名改
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": data_url1
                    }
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": data_url2
                    }
                },
                {"type": "text", "text": "Figure 8. (a) Magnitude responses and (b) phase responses of the DETF resonator   \\mathrm{X}_{1}  under different polarization voltages   V_{\\mathrm{p}}."},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": data_url3
                    }
                },
                {"type": "text", "text": "Figure 9. Resonant frequencies of DETF resonators   X_{1}, X_{2}, Y_{1} , and   Y_{2}  as a function of the polarization voltage   V_{\\mathrm{p}} . ."},
                {
                    "type": "text",
                    "text": prompt_generate_qa_en.format(knowledge = "From the measurement results shown in figure 8, a significant reduction in the resonant frequency for increasing   V_{\\mathrm{p}}  can be observed. Figure 9 plots the frequency shift as a function of the polarization voltage for each DETF resonator in the resonant accelerometer. Due to the fabrication tolerances, these.")
                }
            ]
        }
    ]
)

print(resp.choices[0].message.content)
print(resp.usage.total_tokens)

