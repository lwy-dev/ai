import streamlit as st
import numpy as np
import faiss
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from openai import OpenAI

st.title("PDF知识问答系统")
client = OpenAI(
    api_key="sk-xxx",
    base_url="https://api.deepseek.com",
)
with st.sidebar:
    st.header("文件管理")
    uploaded_file = st.file_uploader("上传PDF文件", type=["pdf"])
    st.caption("支持PDF格式文件")
if uploaded_file:
    for msg in st.session_state.messages[1::]:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
    if "current_file" not in st.session_state or st.session_state.current_file != uploaded_file.name:
        st.session_state.current_file = uploaded_file.name
        st.session_state.messages = [{
            "role": "system",
            "content": "你是PDF知识问答系统"
        }]
        # 删除旧的索引，强制重新处理
        if "index" in st.session_state:
            del st.session_state.index
            del st.session_state.chunks
            del st.session_state.model
        pdf_reader = PdfReader(uploaded_file)
        text=""
        for page in pdf_reader.pages:
            text += page.extract_text()
        chunk_size=500
        chunks=[]
        for i in range (0,len(text),chunk_size):
            chunks.append(text[i:i+chunk_size])
        with st.spinner("加载文件中..."):
            model = SentenceTransformer("BAAI/bge-small-zh-v1.5")
            vectors = model.encode(chunks)
            vectors = np.array(vectors, dtype=np.float32)
            dimension = vectors.shape[1]
            index = faiss.IndexFlatL2(dimension)
            index.add(vectors)
            st.session_state.index = index
            st.session_state.chunks = chunks
            st.session_state.model = model
    model = st.session_state.model
    index = st.session_state.index
    chunks = st.session_state.chunks
    question = st.chat_input("请输入你的问题~")
    if question:
        with st.spinner("检索文件中..."):
            q_vector = model.encode([question])
            q_vector = np.array(q_vector, dtype=np.float32)
            D, I = index.search(q_vector, 3)
            context = ""
            for dix in I[0]:
                context += chunks[dix] + "\n"
        prompt = f"""
        根据PDF的内容回答问题。

        PDF的内容：
        {context}

        问题：
        {question}

        PDF文件里面没有相关的内容就直接说明
        """
        messages = st.session_state.messages.copy()
        messages.append({
            "role": "user",
            "content": prompt
        })
        with st.chat_message("user"):
            st.write(question)
            st.session_state.messages.append({
                "role":"user",
                "content": question
            })
        with st.chat_message("assistant"):
            with st.spinner("思考中..."):
                response=client.chat.completions.create(
                    model="deepseek-chat",
                    messages=messages
                )
                answer=response.choices[0].message.content
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })
            st.write(answer)
else:
    question = st.chat_input("请输入你的问题~")
    if "messages" not in st.session_state:
        st.session_state.messages = [{
            "role": "system",
            "content": "你是AI助手"
        }]
    for msg in st.session_state.messages[1::]:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
    if question:
        st.session_state.messages.append({
            "role": "user",
            "content": question
        })
        with st.chat_message("user"):
            st.write(question)
        with st.chat_message("assistant"):
            with st.spinner("思考中..."):
                response=client.chat.completions.create(
                    model="deepseek-chat",
                    messages=st.session_state.messages
                )
                answer=response.choices[0].message.content
            st.write(answer)
            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })






