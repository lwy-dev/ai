import requests
import json
API_KEY = "sk-934c873666aa4f5c889c46b1fd4c1513"
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