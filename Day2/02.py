import requests
res = requests.get("https://httpbin.org/get")
print(res.text)