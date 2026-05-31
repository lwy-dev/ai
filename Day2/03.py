import requests
import json
API_KEY = "sk-xx"
url = "https://api.deepseek.com/chat/completions"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}
data = {
    "model":"deepseek-chat",
    "messages":[{
        "role":"user",
        "content":"你好"
    }]
}
response = requests.post(url, headers=headers, json=data)
result = response.json()
print(result)