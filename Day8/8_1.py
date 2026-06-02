import streamlit as st
from ollama import chat

st.title("AI助手")
messages = [{
    "role":"system",
    "content":"你是AI助手，专门回答别人的问题"
}]

answer = st.text_input("请输入你的问题：")

if st.button("提交"):
    messages.append({
        "role": "user",
        "content": answer
    })
    response = chat(
        model="deepseek-r1:7b",
        messages=messages,
    )
    st.write(response["message"]["content"])
