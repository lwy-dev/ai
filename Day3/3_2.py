from ollama import chat
messages = []
while True:
    question = input('你：')
    if question == '退出':
        break
    messages.append({
            'role': 'user',
            'content': question
        })
    response = chat(
        model='deepseek-r1:7b',
        messages=messages
    )
    messages.append({
        'role': 'assistant',
        'content': response['message']['content']
    })
    print("AI:",response['message']['content'])