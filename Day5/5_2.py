import requests
import time
API_KEY = "sk-934c873666aa4f5c889c46b1fd4c1513"
url = "https://api.deepseek.com/chat/completions"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}
messages = [{
    'role':'system',
    'content':'你是一名计算机博士老师'
}]
num = 0
f = open("content.txt","w",encoding="utf-8")
f.write(time.strftime("%Y-%m-%d %H:%M:%S\n", time.localtime()))
while True:
    question = input("你：")
    if question == "退出":
        print(f"已安全退出，一共进行了{num}轮对话")
        f.close()
        break
    if question == "清空":
        messages = [{
            'role': 'system',
            'content': '你是一名计算机博士老师'
        }]
        num = 0
        f.close()
        f = open("content.txt", "w", encoding="utf-8")
        f.write(time.strftime("%Y-%m-%d %H:%M:%S\n", time.localtime()))
        print("历史记录已清空")
        continue
    messages.append({
        "role":"user",
        "content":question
    })
    data = {
        "model":"deepseek-chat",
        "messages":messages
    }
    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    # print(result)
    answer = result["choices"][0]["message"]["content"]
    print("AI:",answer)
    num += 1
    f.write("你："+question+"\n")
    f.write("AI："+answer+"\n")
    messages.append({
        "role":"assistant",
        "content":answer
    })