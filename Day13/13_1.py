from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="deepseek-r1:7b")

history = ""

prompt = PromptTemplate(
    input_variables=["history", "question"],
    template="""
以下是历史对话：

{history}

用户问题：

{question}
"""
)

chain = prompt | llm

while True:

    question = input("你：")

    if question == "退出":
        break

    result = chain.invoke({
        "history": history,
        "question": question
    })

    print("AI：", result)

    history += f"\n用户：{question}"
    history += f"\nAI：{result}\n"