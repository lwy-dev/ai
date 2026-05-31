from ollama import chat
response = chat(
    model='deepseek-r1:7b',
    messages=[{
        'role':'user',
        'content':'你好'
    }]
)
print(response['message']['content'])