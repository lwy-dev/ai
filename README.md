# AI 入门学习项目

这是一个按天整理的 AI 入门练习项目，内容从基础概念、环境搭建开始，逐步学习 API 调用、本地大模型运行、Prompt 工程，并完成命令行 AI 聊天机器人。

## 项目内容

| 目录 | 主题 | 主要内容 |
| --- | --- | --- |
| `Day1` | AI 基础与环境搭建 | 了解大模型、API、Prompt、RAG、Agent 等基础概念，安装 Python、Anaconda、编辑器和 Git |
| `Day2` | 调用 AI 接口 | 使用 `requests` 发送 HTTP 请求，学习 JSON、POST 请求，并调用 DeepSeek API |
| `Day3` | 本地运行 AI | 使用 Ollama 运行本地模型 `deepseek-r1:7b`，并通过 Python 调用本地模型 |
| `Day4` | Prompt 工程 | 学习角色设定、Few-shot、思维链、输出格式控制等 Prompt 技巧 |
| `Day5` | AI 聊天机器人项目 | 实现命令行聊天机器人，支持用户输入、AI 回复、历史记忆、清空记录、查看轮数等功能 |
| `Day6` | 环境与版本管理 | 学习 Git、conda、`requirements.txt`、README 编写以及上传 GitHub |

## 目录结构

```text
.
|-- Day1/
|   `-- day1.py
|-- Day2/
|   |-- 01.py
|   |-- 01jeixi.py
|   |-- 02.py
|   |-- 03.py
|   |-- 04.py
|   `-- day2.py
|-- Day3/
|   |-- 3_1.py
|   |-- 3_2.py
|   `-- day3.py
|-- Day4/
|   |-- 4_1.py
|   `-- day4.py
|-- Day5/
|   |-- 5_1.py
|   |-- 5_2.py
|   `-- day5.py
|-- Day6/
|   `-- day6.py
|-- requirements.txt
`-- README.md
```

## 环境要求

- Python 3.10
- Anaconda 或 Miniconda
- Git
- VSCode 或 PyCharm
- 如需运行本地大模型，需要安装 Ollama

## 安装依赖

建议使用 conda 创建独立环境：

```bash
conda create -n ai python=3.10
conda activate ai
pip install -r requirements.txt
```

## 运行方式

### 1. 调用 DeepSeek API

Day2 和 Day5 中有使用 DeepSeek API 的示例：

```bash
python Day2/01.py
python Day5/5_2.py
```

这些脚本会通过 `requests.post()` 向 DeepSeek 聊天接口发送请求，并读取返回结果中的 AI 回复。

### 2. 使用 Ollama 本地模型

先安装 Ollama，并拉取模型：

```bash
ollama pull deepseek-r1:7b
```

然后运行：

```bash
python Day3/3_1.py
python Day3/3_2.py
python Day4/4_1.py
python Day5/5_1.py
```

其中 `Day5/5_1.py` 是本地模型版命令行聊天机器人。

### 3. Streamlit 示例

`Day2/04.py` 使用了 Streamlit：

```bash
streamlit run Day2/04.py
```

## 主要功能

- 使用 Python `requests` 调用在线 AI 接口
- 使用 JSON 组织请求数据
- 支持多轮对话历史
- 使用 Ollama 调用本地大模型
- 使用 system prompt 设置 AI 角色
- 实现命令行 AI 聊天机器人
- 将聊天内容保存到 `content.txt`
- 支持退出、清空历史、查看对话轮数、查看帮助等命令

## 常用命令

在聊天机器人中可以输入：

| 命令 | 作用 |
| --- | --- |
| `退出` | 结束程序 |
| `清空` | 清空历史对话 |
| `轮数` | 查看当前对话轮数 |
| `帮助` | 查看可用命令 |

## 注意事项

1. 代码中出现了 API Key 示例。实际使用时建议改为从环境变量读取，不要把真实密钥提交到 GitHub。
2. `.gitignore` 已忽略 `.env`、`.idea/`、`__pycache__/` 和 `*.pyc`。
3. 运行 DeepSeek API 示例需要联网，并且需要有效的 API Key。
4. 运行 Ollama 示例前，需要确认 Ollama 服务已启动，且本地已下载对应模型。
5. 部分脚本会在当前目录生成 `content.txt`，用于保存聊天记录。

## 学习路线

这个项目适合按下面顺序学习：

1. 先理解 AI 基础概念和 Python 环境。
2. 学会用 `requests` 调用在线 AI API。
3. 学会用 Ollama 在本地运行模型。
4. 练习 Prompt 工程，控制 AI 的角色、任务和输出格式。
5. 完成一个可以连续对话的命令行 AI 聊天机器人。
6. 使用 Git 和 `requirements.txt` 管理项目并上传 GitHub。

## 后续优化方向

- 将 API Key 改为从 `.env` 或系统环境变量读取
- 增加异常处理，例如网络错误、接口返回错误、模型未启动等情况
- 优化中文编码，避免终端显示乱码
- 为聊天机器人增加更清晰的菜单和日志保存格式
- 使用 Streamlit 完成一个可视化聊天界面
