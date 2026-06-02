import streamlit as st
from ollama import chat

st.title("AI知识问答")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "我是一名AI开发老师，专门解答AI知识"}]

for msg in st.session_state.messages[1::]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

question = st.chat_input("请输入你的问题~")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.write(question)
    with st.chat_message("assistant"):
        with st.spinner("AI思考中..."):
            response = chat(
                model="deepseek-r1:7b",
                messages=st.session_state.messages
            )
            answer = response["message"]["content"]
        st.write(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
