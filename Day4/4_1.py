from ollama import chat
response = chat(
    model='deepseek-r1:7b',
    messages=[
        {
            'role':'system',
            'content':'你是精通python的老师',
        },
        {
            'role':'user',
            'content':'用python代码写出1+1=？'
        }
    ]
)
print(response['message']['content'])