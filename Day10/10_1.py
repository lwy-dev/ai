from openai import OpenAI
from pypdf import PdfReader

client = OpenAI(
    api_key="sk-xxx",
    base_url="https://api.deepseek.com"
)

pdf_path = input("请输入PDF路径：")

reader = PdfReader(pdf_path)

test = ""
for page in reader.pages:
    test += page.extract_text()

# print(test)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {
            "role":"system",
            "content":"你是一个文档总结助手"
        },
        {
            "role":"user",
            "content":f"请总结下面PDF内容：\n{test}"
        }
    ]
)

print(response.choices[0].message.content)