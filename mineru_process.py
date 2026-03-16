from pathlib import Path
import asyncio 
from mineru.cli.common import aio_do_parse, read_fn

async def main(): 
    token = "eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJqdGkiOiIxNjEwMDc4MCIsInJvbCI6IlJPTEVfUkVHSVNURVIiLCJpc3MiOiJPcGVuWExhYiIsImlhdCI6MTc3MDI5NTEzNCwiY2xpZW50SWQiOiJsa3pkeDU3bnZ5MjJqa3BxOXgydyIsInBob25lIjoiIiwib3BlbklkIjpudWxsLCJ1dWlkIjoiZTIzYzkyNGMtNDIzZi00Yzc5LWJhOWEtNDRlNmFjY2UyMzE5IiwiZW1haWwiOiIiLCJleHAiOjE3NzE1MDQ3MzR9.mbO2nAs4JcZNqm-NUHyn02NF5yiGTr6kMSIjW0eYlttoTtqsNnPqTPM-PtrUk_4e-_MPve7J4cuDPqqLLpNgvw"
    try:
        # 1. 获取所有支持的文件  
        text_resources_dir = "./pdf_resources"
        supported_extensions = [".pdf", ".png", ".jpeg", ".jpg", ".tiff", ".bmp", ".webp"]  
        file_paths = []  
        
        for ext in supported_extensions:  
            file_paths.extend(Path(text_resources_dir).glob(f"*{ext}"))  
        
        if not file_paths:  
            print(f"在 {text_resources_dir} 中未找到支持的文件")  
        else:
            pdf_file_names = []  
            pdf_bytes_list = []  
            p_lang_list = []  
            
            for file_path in file_paths:  
                try:  
                    # 读取文件字节  
                    pdf_bytes = read_fn(str(file_path))  
                    pdf_bytes_list.append(pdf_bytes)  
                    pdf_file_names.append(file_path.stem)  
                    p_lang_list.append("en")  # 默认中文，可根据需要调整  
                except Exception as e:  
                    print(f"读取文件失败 {file_path}: {e}")  
                    continue  


            await aio_do_parse(
                output_dir="./text_resources",
                pdf_file_names=pdf_file_names,
                pdf_bytes_list=pdf_bytes_list,
                p_lang_list=["en"],
                backend="vlm-auto-engine",
                parse_method="auto",
                formula_enable=True,
                table_enable=True,
                f_draw_layout_bbox=False,     # Skip layout.pdf  
                f_draw_span_bbox=False,       # Skip span.pdf  
                f_dump_orig_pdf=False,        # Skip original PDF copy     
                f_dump_middle_json=False,
                f_dump_model_output=False,
            )
            
            print(f"处理完成，结果保存在: text_resources")  
    


    except Exception as err:
        print(err)

if __name__ == "__main__":  
    asyncio.run(main())