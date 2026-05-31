import requests
API_KEY = "sk-934c873666aa4f5c889c46b1fd4c1513"
url = "https://api.deepseek.com/chat/completions"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}
messages = []
while True:
    question = input("你：")
    if question == "退出":
        break
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
    messages.append({
        "role":"assistant",
        "content":answer
    })