# 整体结构
# 你可以把整个程序理解成：
# 1. 导入工具
# 2. 创建网页标题
# 3. 创建聊天记录仓库
# 4. 显示历史聊天记录
# 5. 等待用户输入
# 6. 用户发送消息
# 7. 调用AI
# 8. 显示AI回复
# 9. 保存AI回复
# ---
# 第一部分
# import streamlit as st
# from ollama import chat
# 作用
# 导入需要使用的库。
# ---
# 第一行
# import streamlit as st
# 相当于：
# import streamlit
# 但是太长了。
# 所以取别名：
# st
# 以后写：
# st.title()
# st.write()
# st.chat_input()
# 更方便。
# ---
# 第二行
# from ollama import chat
# 导入 Ollama 的聊天函数。
# 以后：
# response = chat(...)
# 就能调用本地大模型。
# ---
# 第二部分
# st.title("AI聊天机器人")
# 作用：
# 网页标题。
# 显示：
# AI聊天机器人
# ==========
# ---
# 如果删掉：
# st.title()
# 网页仍然能运行。
# 只是没有标题。
# ---
# 第三部分
# if "messages" not in st.session_state:
#     st.session_state.messages = []
# 这是最重要的部分之一。
# ---
# 先理解什么是 session_state
# 你可以把它理解成：
# 一个保险箱
# 专门存数据。
# ---
# 例如：
# st.session_state.messages
# 就是：
# 聊天记录仓库
# ---
# 第一次运行
# 此时：
# st.session_state
# 里面什么都没有。
# ---
# 所以：
# "messages" not in st.session_state
# 结果：
# True
# ---
# 于是执行：
# st.session_state.messages = []
# 创建空列表。
# 变成：
# []
# ---
# 意思：
# 聊天记录为空
# ---
# 第四部分
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.write(msg["content"])
# 作用：
# 显示历史聊天记录。
# ---
# 假设：
# st.session_state.messages
# 里面有：
# [
#     {
#         "role":"user",
#         "content":"你好"
#     },
#
#     {
#         "role":"assistant",
#         "content":"你好呀"
#     }
# ]
# ---
# 第一次循环
# msg =
# {
#     "role":"user",
#     "content":"你好"
# }
# ---
# 执行：
# with st.chat_message("user"):
# 显示：
# 👤
# ---
# 执行：
# st.write("你好")
# 显示：
# 👤 你好
# ---
# 第二次循环
# msg =
# {
#     "role":"assistant",
#     "content":"你好呀"
# }
# ---
# 显示：
# 🤖 你好呀
# ---
# 最终：
# 👤 你好
# 🤖 你好呀
# ---
# 第五部分
# question = st.chat_input("请输入问题")
# 作用：
# 创建聊天输入框。
# ---
# 显示：
# 请输入问题...
# ---
# 用户输入：
# 什么是Python
# ---
# 变量：
# question
# 得到：
# "什么是Python"
# ---
# 第六部分
# if question:
# 意思：
# if question != "":
# ---
# 如果用户没输入：
# question = ""
# 程序不执行下面代码。
# ---
# 如果用户输入：
# question = "你好"
# 进入下面逻辑。
# ---
# 第七部分
# st.session_state.messages.append(
#     {
#         "role":"user",
#         "content":question
#     }
# )
# 作用：
# 保存用户消息。
# ---
# 例如：
# 用户输入：
# 你好
# ---
# 保存后：
# [
#     {
#         "role":"user",
#         "content":"你好"
#     }
# ]
# ---
# 如果继续聊天：
# 什么是Python
# 变成：
# [
#     {
#         "role":"user",
#         "content":"你好"
#     },
#
#     {
#         "role":"assistant",
#         "content":"你好呀"
#     },
#
#     {
#         "role":"user",
#         "content":"什么是Python"
#     }
# ]
# ---
# 第八部分
# with st.chat_message("user"):
#     st.write(question)
# 作用：
# 立即显示用户消息。
# ---
# 显示：
# 👤 什么是Python
# ---
# 为什么要写？
# 因为 AI 可能思考 5 秒。
# 如果不显示：
# 用户会以为没发出去
# ---
# 第九部分
# with st.chat_message("assistant"):
# 创建 AI 气泡。
# ---
# 显示：
# 🤖
# ---
# 后面的内容都在这个气泡里显示。
# ---
# 第十部分
# with st.spinner("AI思考中..."):
# 作用：
# 显示加载动画。
# ---
# 用户看到：
# 🤖
# AI思考中...
# ---
# 这样不会觉得程序卡死。
# ---
# 第十一部分
# response = chat(
#     model="deepseek-r1:7b",
#     messages=st.session_state.messages
# )
# 这是整个程序最核心的一行。
# ---
# 此时：
# st.session_state.messages
# 可能是：
# [
#     {
#         "role":"user",
#         "content":"你好"
#     },
#
#     {
#         "role":"assistant",
#         "content":"你好呀"
#     },
#
#     {
#         "role":"user",
#         "content":"什么是Python"
#     }
# ]
# ---
# 全部发给模型。
# 相当于：
# 用户：你好
# AI：你好呀
# 用户：什么是Python
# 一起发送。
# ---
# 所以 AI 才有：
# 上下文记忆
# ---
# 第十二部分
# answer = response["message"]["content"]
# 假设返回：
# {
#     "message":
#     {
#         "content":"Python是一门高级编程语言"
#     }
# }
# ---
# 取出：
# "Python是一门高级编程语言"
# 保存到：
# answer
# ---
# 第十三部分
# st.write(answer)
# 显示：
# 🤖 Python是一门高级编程语言
# ---
# 用户终于看到回答。
# ---
# 第十四部分
# st.session_state.messages.append(
#     {
#         "role":"assistant",
#         "content":answer
#     }
# )
# 保存 AI 回复。
# ---
# 最终：
# [
#     {
#         "role":"user",
#         "content":"你好"
#     },
#
#     {
#         "role":"assistant",
#         "content":"你好呀"
#     },
#
#     {
#         "role":"user",
#         "content":"什么是Python"
#     },
#
#     {
#         "role":"assistant",
#         "content":"Python是一门高级编程语言"
#     }
# ]
# ---
# 一张图看懂整个流程
# 用户输入问题
#       ↓
# st.chat_input()
#       ↓
# 保存用户消息
# messages.append()
#       ↓
# 立即显示用户消息
# chat_message("user")
#       ↓
# 显示AI思考中
# spinner()
#       ↓
# 调用Ollama
# chat()
#       ↓
# 获取AI回复
# answer
#       ↓
# 显示AI回复
# st.write()
#       ↓
# 保存AI回复
# messages.append()
#       ↓
# 等待下一轮聊天
# 如果老师答辩时问你：
# > 为什么要用 st.session_state.messages？
# 你可以回答：
# > 因为 Streamlit 每次交互都会重新执行脚本，所以需要用 st.session_state 保存聊天记录。这样既能显示历史消息，也能把上下文发送给模型，实现连续对话。
