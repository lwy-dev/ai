# 这份代码其实是你前面学过的很多知识的集合：
# Streamlit
# +
# PDF读取
# +
# Embedding
# +
# 向量数据库
# +
# RAG
# +
# Agent
# +
# DeepSeek
# 如果你把这份代码彻底搞懂，后面比赛里的很多项目都能看懂。
# ---
# 整体流程图
# 你的程序运行流程：
# 启动网页
#     ↓
# 上传PDF
#     ↓
# 读取PDF内容
#     ↓
# 切Chunk
#     ↓
# Embedding向量化
#     ↓
# FAISS建立索引
#     ↓
# 用户提问
#     ↓
# Agent
#     ↓
# 知识库工具
#     ↓
# 检索相关内容
#     ↓
# DeepSeek回答
#     ↓
# 显示结果
# ---
# 第一部分 导入库
# import streamlit as st
# from pypdf import PdfReader
# from sentence_transformers import SentenceTransformer
# from ollama import chat
# import faiss
# import numpy as np
# ---
# streamlit
# 负责网页
# 例如：
# st.title()
# st.write()
# st.button()
# 都是它的功能。
# ---
# PdfReader
# 负责读取PDF。
# 例如：
# reader = PdfReader(file)
# 就能打开PDF。
# ---
# SentenceTransformer
# 负责Embedding。
# 例如：
# 你好
# 变成：
# [0.21,0.58,0.77...]
# 这种向量。
# ---
# ollama
# 负责调用本地大模型。
# 例如：
# chat(
#     model="deepseek-r1:7b"
# )
# ---
# faiss
# 向量数据库。
# 负责：
# 找最相似内容
# ---
# numpy
# 处理数组。
# FAISS要求：
# float32
# 所以必须用。
# ---
# 第二部分 页面标题
# st.title("🤖 知识库Agent")
# 网页显示：
# 🤖 知识库Agent
# ---
# 第三部分 上传PDF
# uploaded_file = st.file_uploader(
#     "上传PDF文件",
#     type=["pdf"]
# )
# 生成：
# 选择文件
# 按钮。
# ---
# 上传成功后：
# if uploaded_file:
# 成立。
# 开始执行后面代码。
# ---
# 第四部分 读取PDF
# reader = PdfReader(uploaded_file)
# 打开PDF。
# ---
# 创建变量：
# text = ""
# 用于保存全文。
# ---
# 遍历每一页：
# for page in reader.pages:
# 例如：
# 第1页
# 第2页
# 第3页
# ---
# 读取文字：
# page_text = page.extract_text()
# ---
# 拼接：
# text += page_text
# 最终：
# 整个PDF内容
# 都在：
# text
# 里面。
# ---
# 第五部分 Chunk切分
# chunk_size = 500
# 表示：
# 500个字符一块
# ---
# 为什么切？
# 假设PDF：
# 10000字
# 不能直接Embedding。
# 太长。
# ---
# 于是：
# for i in range(
#     0,
#     len(text),
#     chunk_size
# ):
# 每500字切一次。
# ---
# 例如：
# Chunk1
# Chunk2
# Chunk3
# Chunk4
# 存入：
# chunks
# 列表。
# ---
# 第六部分 加载Embedding模型
# model = SentenceTransformer(
#     "BAAI/bge-small-zh-v1.5"
# )
# 这是中文向量模型。
# 作用：
# 文字
# ↓
# 向量
# ---
# 例如：
# model.encode("什么是RAG")
# 变成：
# 384维向量
# 类似：
# [0.23,0.55,0.88...]
# ---
# 第七部分 所有Chunk向量化
# vectors = model.encode(chunks)
# 例如：
# Chunk1
# ↓
# 向量1
# Chunk2
# ↓
# 向量2
# Chunk3
# ↓
# 向量3
# ---
# 得到：
# vectors
# ---
# 第八部分 转numpy
# vectors = np.array(
#     vectors,
#     dtype=np.float32
# )
# 因为：
# faiss
# 只能接受：
# float32
# 格式。
# ---
# 第九部分 建立FAISS索引
# 获取向量维度：
# dimension = vectors.shape[1]
# 对于：
# bge-small
# 通常：
# 384维
# ---
# 建立索引：
# index = faiss.IndexFlatL2(
#     dimension
# )
# 意思：
# 用L2距离搜索
# 即欧氏距离。
# ---
# 加入数据：
# index.add(vectors)
# 此时：
# 向量数据库建立完成
# ---
# 第十部分 知识库工具
# def search_knowledge(question):
# 这是 Day16 的核心。
# ---
# 用户问题：
# 什么是RAG
# ---
# 向量化：
# q_vector = model.encode(
#     [question]
# )
# 变成：
# 问题向量
# ---
# 搜索：
# D,I = index.search(
#     q_vector,
#     3
# )
# 意思：
# 找最相似的3段内容
# ---
# 例如：
# Chunk15
# Chunk22
# Chunk30
# ---
# 拼接：
# context += chunks[idx]
# 得到：
# 相关知识
# 返回。
# ---
# 第十一部分 Agent
# def agent(question):
# 这里是 Agent。
# ---
# Agent收到：
# 什么是RAG
# ---
# 先调用工具：
# context = search_knowledge(
#     question
# )
# ---
# 得到：
# RAG相关内容
# ---
# 然后组织Prompt：
# prompt = f"""
# 根据知识库内容回答：
# ...
# """
# ---
# 最终变成：
# 知识库内容：
# xxxxx
# 问题：
# 什么是RAG
# ---
# 第十二部分 调用DeepSeek
# response = chat(
#     model="deepseek-r1:7b",
#     ...
# )
# 调用：
# DeepSeek-R1
# ---
# 返回：
# response["message"]["content"]
# 即：
# AI回答
# ---
# 第十三部分 用户提问
# question = st.text_input(
#     "请输入你的问题"
# )
# 网页出现：
# 请输入你的问题
# 输入框。
# ---
# 第十四部分 最终执行
# answer = agent(question)
# 执行：
# Agent
# ↓
# 知识库工具
# ↓
# FAISS检索
# ↓
# DeepSeek
# ↓
# 答案
# ---
# 这份代码最重要的面试题
# 如果比赛评委问你：
# > Agent在哪里？
# 你直接回答：
# agent()函数就是Agent。
# search_knowledge()函数就是知识库工具。
# Agent接收用户问题后，
# 调用知识库工具检索相关内容，
# 然后把检索结果交给DeepSeek生成最终答案。
# 整体流程是：
# 用户
# ↓
# Agent
# ↓
# Tool
# ↓
# RAG
# ↓
# LLM
# ↓
# Answer
# 如果你能把这段逻辑讲清楚，说明你已经真正理解了 Day12～Day16 这一阶段的核心知识。