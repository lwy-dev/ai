# ---
# 第一部分
# import requests
# 意思：
# 导入 requests 库
# ---
# requests 是干嘛的？
# 作用：
# 让 Python 能联网
# ---
# 没有它
# Python：
# 无法调用AI
# ---
# 有了它
# Python 才能：
# 发送API请求
# ---
# 第二部分
# API_KEY = "sk-xxxxxxxx"
# ---
# 这是你的 API 密钥
# 相当于：
# “身份证”
# “钥匙”
# ---
# DeepSeek 怎么知道是你？
# 靠这个：
# API_KEY
# ---
# 第三部分
# url = "https://api.deepseek.com/chat/completions"
# ---
# 这是接口地址
# 你可以理解成：
# “DeepSeek 的电话号码”
# ---
# 你的程序会向这里发请求
# 就像：
# 给AI打电话
# ---
# 第四部分（重点）
# headers = {
#     "Authorization": f"Bearer {API_KEY}",
#     "Content-Type": "application/json"
# }
# ---
# headers 是什么？
# 它是：
# 请求头
# ---
# 请求头作用
# 相当于：
# “告诉服务器你的身份和数据类型”
# ---
# 第一行
# "Authorization": f"Bearer {API_KEY}"
# 意思：
# “我是合法用户”
# ---
# Bearer 是什么？
# 一种认证格式。
# 服务器看到：
# Bearer sk-xxxx
# 就知道：
# 你在用 API Key 登录
# ---
# 第二行
# "Content-Type": "application/json"
# 意思：
# “我发送的数据是 JSON 格式”
# ---
# 第五部分
# messages = []
# ---
# messages 是什么？
# 这是：
# 聊天记录
# ---
# 为什么需要它？
# 因为：
# AI本身不会记忆。
# ---
# 你必须把历史聊天：
# 重新发给AI
# AI才会：
# “记得上下文”
# ---
# 第六部分（循环）
# while True:
# ---
# 意思：
# 无限循环
# 程序会一直运行。
# ---
# 相当于：
# 一直聊天
# ---
# 第七部分
# question = input("你：")
# ---
# input 是什么？
# 作用：
# 等待用户输入
# ---
# 比如：
# 你输入：
# 你好
# 变量：
# question
# 就会变成：
# "你好"
# ---
# 第八部分
# if question == "退出":
#     break
# ---
# 意思：
# 如果用户输入：
# 退出
# 程序结束。
# ---
# break
# 作用：
# 跳出循环
# ---
# 第九部分（非常重要）
# messages.append({
#     "role":"user",
#     "content":question
# })
# ---
# append 是什么？
# 作用：
# 往列表里添加内容
# ---
# 添加后
# messages 变成：
# [
#     {
#         "role":"user",
#         "content":"你好"
#     }
# ]
# ---
# role 是什么？
# 表示：
# “谁说的话”
# ---
# user
# 表示：
# 用户说的话
# ---
# assistant
# 表示：
# AI说的话
# ---
# 第十部分
# data = {
#     "model":"deepseek-chat",
#     "messages":messages
# }
# ---
# data 是什么？
# 这是：
# 发送给 AI 的数据
# ---
# model
# 表示：
# 使用哪个模型
# ---
# messages
# 表示：
# 聊天记录
# ---
# 第十一部分（核心）
# response = requests.post(
#     url,
#     headers=headers,
#     json=data
# )
# ---
# 这是整个程序最核心的一句
# 意思：
# 向 DeepSeek 发送 POST 请求
# ---
# 发送了什么？
# url
# headers
# json数据
# ---
# 本质：
# 你的程序
# ↓
# 联网
# ↓
# 把问题发给AI
# ---
# 第十二部分
# result = response.json()
# ---
# response 是什么？
# 服务器返回的数据。
# ---
# response.json()
# 作用：
# 把 JSON 转成 Python字典
# ---
# 比如：
# 服务器返回：
# {
#   "name":"小明"
# }
# 会变成：
# {
#     "name":"小明"
# }
# ---
# 第十三部分（重点）
# answer = result["choices"][0]["message"]["content"]
# ---
# 这里是在：
# 提取 AI 回复内容
# ---
# result 长这样
# {
#   "choices": [
#     {
#       "message": {
#         "content": "你好！"
#       }
#     }
#   ]
# }
# ---
# 所以：
# ["choices"]
# 拿到：
# [
#    ...
# ]
# ---
# [0]
# 表示：
# 第一个回答
# ---
# ["message"]
# 拿到：
# {
#    "content":"你好"
# }
# ---
# ["content"]
# 最终拿到：
# "你好"
# ---
# 第十四部分
# print("AI:",answer)
# ---
# 作用：
# 打印 AI 回复。
# ---
# 第十五部分（非常关键）
# messages.append({
#     "role":"assistant",
#     "content":answer
# })
# ---
# 为什么必须加这个？
# 因为：
# 要保存 AI 回复
# ---
# 否则下一轮：
# AI会失忆。
# ---
# 加入后
# messages 变成：
# [
#   {
#     "role":"user",
#     "content":"你好"
#   },
#   {
#     "role":"assistant",
#     "content":"你好！"
#   }
# ]
# ---
# 下一轮发送时
# AI就知道：
# 之前聊过什么
# ---
# 你的整个程序运行流程（必须理解）
# 用户输入问题
#       ↓
# 加入messages
#       ↓
# 构造JSON数据
#       ↓
# requests.post发送请求
#       ↓
# DeepSeek收到问题
#       ↓
# AI生成回答
#       ↓
# 返回JSON
#       ↓
# response.json()
#       ↓
# 提取content
#       ↓
# print打印
#       ↓
# 保存AI回复
#       ↓
# 进入下一轮聊天
# ---
# 你今天真正学会的东西
# 你已经开始真正理解：
# 技术	你已经接触
# Python	基础语法
# requests	网络请求
# API	AI接口
# JSON	数据结构
# POST请求	提交数据
# 多轮对话	上下文记忆
# 大模型调用	AI开发核心
# 这已经是：
# 真正 AI 应用开发入门了。