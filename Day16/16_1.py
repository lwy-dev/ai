import streamlit as st
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from ollama import chat
import faiss
import numpy as np

st.title("🤖 知识库Agent")

# 上传PDF
uploaded_file = st.file_uploader(
    "上传PDF文件",
    type=["pdf"]
)

if uploaded_file:

    st.success("PDF上传成功！")

    # 读取PDF
    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    st.write(f"读取完成，共 {len(text)} 个字符")

    # Chunk切分
    chunk_size = 500

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    st.write(f"共切分 {len(chunks)} 个Chunk")

    # 加载Embedding模型
    with st.spinner("正在加载向量模型..."):

        model = SentenceTransformer(
            "BAAI/bge-small-zh-v1.5"
        )

        vectors = model.encode(chunks)

    vectors = np.array(
        vectors,
        dtype=np.float32
    )

    # 建立FAISS索引
    dimension = vectors.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(vectors)

    st.success("向量库建立成功")

    # =========================
    # 知识库工具
    # =========================
    def search_knowledge(question):

        q_vector = model.encode([question])

        q_vector = np.array(
            q_vector,
            dtype=np.float32
        )

        D, I = index.search(
            q_vector,
            3
        )

        context = ""

        for idx in I[0]:
            context += chunks[idx] + "\n"

        return context

    # =========================
    # Agent
    # =========================
    def agent(question):

        st.info("Agent正在思考...")

        # 调用知识库工具
        context = search_knowledge(question)

        prompt = f"""
根据以下知识库内容回答问题。

知识库内容：
{context}

问题：
{question}

如果知识库中没有相关内容，请直接说明。
"""

        response = chat(
            model="deepseek-r1:7b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    # 用户提问
    question = st.text_input(
        "请输入你的问题"
    )

    if question:

        with st.spinner("Agent正在处理..."):

            answer = agent(question)

        st.subheader("回答结果")

        st.write(answer)