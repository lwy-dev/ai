import streamlit as st
import requests

API_KEY = "sk-xxxxxxxxxxxxxx"
url = "https://api.deepseek.com/chat/completions"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

st.title("AI知识问答")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "你是一名AI开发老师，专门解答AI知识"}]

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
            data = {
                "model":"deepseek-chat",
                "messages":st.session_state.messages,
            }
            response = requests.post(url, headers=headers, json=data)
            result = response.json()
            answer = result["choices"][0]["message"]["content"]
        st.write(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
