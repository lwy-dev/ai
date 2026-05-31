from ollama import chat
import time
f = open("content.txt","w",encoding="utf-8")
f.write(time.strftime("%Y-%m-%d %H:%M:%S\n", time.localtime()))
system = {
                'role':'system',
                'content':'你是AI助手',
            }
messages = [system]
num = 0
print("退出：结束程序")
print("清空：清除历史记录")
print("轮数：查看聊天记录")
print("帮助：查看命令")
while True:
    question = input("lwy:")
    if question == '退出':
        print(f"已安全退出并且对话记录已保存在content.text中")
        f.close()
        break
    if question == '清空':
        messages = [system]
        f.close()
        f = open("content.txt", "w", encoding="utf-8")
        f.write(time.strftime("%Y-%m-%d %H:%M:%S\n", time.localtime()))
        print("历史记录已清空")
        continue
    if question == "轮数":
        print(f"当前已进行了{num}轮对话")
        continue
    if question == "帮助":
        print("退出：结束程序")
        print("清空：清除历史记录")
        print("轮数：查看聊天记录")
        print("帮助：查看命令")
        continue
    messages.append(
        {
            'role':'user',
            'content':question
        })
    response = chat(
        model='deepseek-r1:7b',
        messages=messages
    )
    f.write("lwy:"+question+"\n")
    f.write("AI:"+response['message']['content']+"\n")
    print(response['message']['content'])
    num += 1
    messages.append(
        {
            'role':'assistant',
            'content':response['message']['content']
        })