# Using open-webui REST APIs, chats using the knowledge collection

import requests
from pathlib import Path

token = Path('.token.txt').read_text().strip()
model = f'llama3.2:1b'
k_id = 'a00fb432-7144-482b-b09b-3e9bd4de4ef6'

def chat_with_collection(token, model, query, collection_id):
    url = 'http://localhost:8080/api/chat/completions'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    payload = {
        'model': model,
        'messages': [{'role': 'user', 'content': query}],
        'files': [{'type': 'collection', 'id': collection_id}]
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()


q = f'What is rolling start?'

ret = chat_with_collection(token, model, q, k_id)
#print(f'Asking question to the knowledge {ret = }')
#print(f'{ret = }')
print(f'{ret["choices"][0]["message"]["content"]}')
