from pdf2image import convert_from_path
import os
from dotenv import load_dotenv
from openai import OpenAI
import base64
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser(
    prog="pdf2md",
    description="A tool that converts PDF documents to Markdown format using OpenAI's vision model",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
parser.add_argument("input", type=str, help="Path to the input PDF file")
parser.add_argument("--output", "-o", type=str, default="output.md", help="Path to the output Markdown file")
args = parser.parse_args()
input_file = args.input
output_file = args.output

load_dotenv()
base_url = os.getenv("OPENAI_BASE_URL")
llm_model = os.getenv("OPENAI_LLM_MODEL", default="gpt-4o")
client = OpenAI(base_url=base_url)

images = convert_from_path(input_file)
output_folder = "output"
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

with open(output_file, "w") as f:
    for i, image in enumerate(tqdm(images[:2])):
        image_name = f"{output_folder}/image_{i}.jpg"
        image.save(image_name, "JPEG")
        data_uri = ""
        with open(image_name, "rb") as image_file:
            image_base64 = base64.b64encode(image_file.read()).decode("utf-8")
            data_uri = f"data:image/jpeg;base64,{image_base64}"

        response = client.chat.completions.create(
            model=llm_model,
            messages=[
                {
                    "role": "developer",
                    "content": "请把用户上传的图片翻译成markdown格式的文本，注意你回答的内容将直接写入到output.md文件中，故不要包含多余的信息，也不要用代码块包围markdown文本。对于行内公式，应该用$...$而不是\(...\)，$...$要和周围的中文汉字有一个空格的间隔，和标点符号不用。对于行间公式，应该用$$...$$而不是\[...\]。",
                },
                {
                    "role": "user",
                    "content": [{"type": "image_url", "image_url": {"url": data_uri}}],
                },
            ],
        )
        f.write(response.choices[0].message.content + "\n")
