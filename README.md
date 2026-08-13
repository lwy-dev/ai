# AI 入门学习项目

这是一个按天整理的 AI 入门练习项目，从基础概念、环境搭建开始，逐步学习 API 调用、本地大模型运行、Prompt 工程、Streamlit 网页应用、RAG 知识库问答、Agent、视觉识别与 PyTorch 推理，最终完成一个完整的多模态 AI 流程。

## 项目内容

| 目录 | 主题 | 主要内容 |
| --- | --- | --- |
| `Day1` | AI 基础与环境搭建 | 大模型、API、Prompt、RAG、Agent 概念；安装 Python、Anaconda、编辑器、Git |
| `Day2` | 调用 AI 接口 | 使用 `requests` 发送 HTTP 请求，学习 JSON、POST，调用 DeepSeek API |
| `Day3` | 本地运行 AI | 使用 Ollama 运行 `deepseek-r1:7b`，并通过 Python 调用本地模型 |
| `Day4` | Prompt 工程 | 角色设定、Few-shot、思维链、输出格式控制等 Prompt 技巧 |
| `Day5` | 命令行聊天机器人 | 支持用户输入、AI 回复、历史记忆、清空、轮数、帮助等命令 |
| `Day6` | 环境与版本管理 | Git、Conda、Docker、`requirements.txt`、README、上传 GitHub |
| `Day7` | 第一周复现 | 独立重做 API 调用、本地 AI、聊天机器人 |
| `Day8` | Streamlit 网页 | `st.title`、`st.button`、`st.text_input`，做第一个网页 |
| `Day9` | 网页聊天机器人 | `st.chat_input`、`st.chat_message`、`st.session_state` 实现网页版聊天 |
| `Day10` | 文件读取 | 读取 txt/csv/pdf，使用 Pandas 处理数据，AI 总结 PDF |
| `Day11` | RAG 概念 | Embedding、Chunk 切分、向量检索，理解 RAG 完整流程 |
| `Day12` | 第一个 RAG | PDF 问答系统：FAISS 向量检索 + 本地模型回答 |
| `Day13` | LangChain | `PromptTemplate` + `OllamaLLM` 实现带记忆的多轮对话 |
| `Day14` | PDF 知识问答系统 | Streamlit + FAISS + DeepSeek，侧边栏上传 PDF、连续问答 |
| `Day15` | Dify 与 API 服务 | 安装 Dify（工作流/Agent/知识库）；FastAPI 天气查询服务 |
| `Day16` | 知识库 Agent | 上传文档问答，Agent + 知识库工具 + FAISS + DeepSeek |
| `Day17` | OpenCV 基础 | `cv2.imread`、打开摄像头、读取视频流 |
| `Day18` | AI 图片识别 | 上传图片，调用 Ollama 的 `llava` 多模态模型描述图片 |
| `Day19` | PyTorch 基础 | Tensor、加载 ResNet18 预训练模型、推理与类别预测 |
| `Day20` | 完整 AI 流程 | 图片 → OpenCV → AI 分析 → 输出结果 |

此外：

- `test.py`：使用 PaddleOCR 做中文文字识别（OCR）。
- `dify/`：Dify 开源项目源码，用于 Day15 的 Dify 学习与部署。

## 目录结构

```text
.
|-- Day1/  ... Day20/       # 按天整理的学习内容
|   |-- dayN.py             # 当日目标与任务说明
|   |-- N_1.py 等           # 示例 / 解析代码
|   `-- noteN.txt           # 笔记（Day1 ~ Day9）
|-- dify/                   # Dify 开源项目
|-- test.py                 # PaddleOCR 示例
|-- requirements.txt        # 依赖清单
|-- .env                    # 环境变量（已加入 .gitignore）
`-- README.md
```

## 环境要求

- Python 3.10+
- Anaconda 或 Miniconda
- Git
- VSCode 或 PyCharm
- Ollama（运行本地大模型，需先拉取模型）
- 可选：Docker（Day6、Day15 部署 Dify）

## 安装依赖

建议使用 Conda 创建独立环境：

```bash
conda create -n ai python=3.10
conda activate ai
pip install -r requirements.txt
```

## 运行方式

### 1. 调用 DeepSeek API

```bash
python Day2/01.py
python Day5/5_2.py
```

这些脚本通过 `requests.post()` 调用 DeepSeek 聊天接口，需要联网并配置有效的 `API_KEY`（可在 `.env` 或代码中设置）。

### 2. 使用 Ollama 本地模型

先安装 Ollama 并拉取模型：

```bash
ollama pull deepseek-r1:7b
ollama pull llava
```

```bash
python Day3/3_1.py
python Day3/3_2.py
python Day4/4_1.py
python Day5/5_1.py
```

### 3. Streamlit 网页应用

```bash
streamlit run Day2/04.py          # 第 2 天 Streamlit 示例
streamlit run Day9/9_1.py         # 网页聊天机器人（本地模型）
streamlit run Day12/12_1.py       # PDF 问答系统
streamlit run Day14/14_1.py       # PDF 知识问答系统（DeepSeek）
streamlit run Day16/16_1.py       # 知识库 Agent
streamlit run Day18/18_1.py       # AI 图片识别助手（llava）
```

注意：Streamlit 应用必须用 `streamlit run` 启动，不能用 `python xxx.py` 运行，否则会出现 `missing ScriptRunContext` 等问题。

### 4. OpenCV / PyTorch

```bash
python Day17/17_1.py              # 显示图片
python Day17/17_2.py              # 打开摄像头
python Day17/17_3.py              # 读取视频
python Day19/19_1.py              # ResNet18 推理
python Day19/19_3.py              # 图片分类预测
```

### 5. FastAPI 天气服务（Day15）

```bash
uvicorn main:app --host 0.0.0.0 --port 8081
# 或
python Day15/main.py
```

## 主要功能与技术栈

- `requests` / `openai`：调用在线大模型 API
- `ollama`：本地运行并调用大模型
- `streamlit`：快速搭建网页应用
- `langchain`：Prompt 模板与链式调用
- `sentence-transformers` + `faiss`：Embedding 与向量检索（RAG）
- `pypdf` / `pandas`：PDF、CSV 等文件读取与处理
- `opencv-python`：图像读取、摄像头与视频流
- `torch` + `torchvision`：加载预训练模型并推理
- `fastapi` + `uvicorn`：构建 API 服务
- `paddleocr`：中文 OCR 文字识别

## 学习路线

建议按以下顺序学习：

1. 理解 AI 基础概念，搭建 Python 环境（Day1）。
2. 用 `requests` 调用在线 AI API（Day2）。
3. 用 Ollama 在本地运行模型（Day3）。
4. 练习 Prompt 工程，控制角色、任务与输出格式（Day4）。
5. 完成命令行聊天机器人（Day5）。
6. 掌握 Git、Conda、Docker 等环境与版本管理（Day6）。
7. 独立复现第一周成果（Day7）。
8. 学习 Streamlit 制作网页（Day8），完成网页聊天机器人（Day9）。
9. 读取文件并用 AI 总结 PDF（Day10）。
10. 理解 RAG 并完成 PDF 问答系统（Day11~Day12）。
11. 学习 LangChain 与知识库 Agent（Day13~Day16）。
12. 学习 OpenCV 与多模态图片识别（Day17~Day18）。
13. 学习 PyTorch 推理，串联完整 AI 流程（Day19~Day20）。

## 注意事项

1. 请勿将真实的 API Key 提交到 GitHub。`.env` 已加入 `.gitignore`，建议统一从环境变量或 `.env` 读取密钥。
2. 运行 DeepSeek API 示例需要联网并配置有效 API Key。
3. 运行 Ollama 示例前需确认 Ollama 服务已启动，且已下载对应模型（`deepseek-r1:7b`、`llava` 等）。
4. 运行 `Day12`/`Day14`/`Day16` 前，首次会下载 Embedding 模型 `BAAI/bge-small-zh-v1.5`，需要联网。
5. `Day19` 首次运行会下载 ResNet18 预训练权重。
6. `test.py` 依赖 PaddleOCR，需单独安装：`pip install paddleocr paddlepaddle`。
