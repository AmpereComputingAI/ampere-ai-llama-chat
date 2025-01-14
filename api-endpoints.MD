# API Endpoints
This guide provides essential information on how to interact with the API endpoints effectively to achieve seamless integration and automation using the models

## Authentication
To ensure secure access to the API, authentication is required️. You can authenticate your API requests using the Bearer Token mechanism. Obtain your API key from Settings->Account in the Open WebUI, or alternatively, use a JWT (JSON Web Token) for authentication.

## Swagger Documentation Links
Make sure to set the ENV environment variable to 'dev' in order to access the Swagger documentation for any of these services.
Access detailed API documentation for different services provided by Open WebUI
```
http://<server-IP>:8080/docs
```

## Notable API Endpoints
#### Retrieve All Models
##### Curl Example
```
curl -H "Authorization: Bearer YOUR_API_KEY" http://localhost:8080/api/models
```

### Retrieval Augmented Generation (RAG)
#### Uploading Files
```
import requests

def upload_file(token, file_path):
    url = 'http://localhost:8080/api/v1/files/'
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json'
    }
    files = {'file': open(file_path, 'rb')}
    response = requests.post(url, headers=headers, files=files)
    return response.json()

ret = upload_file(token, file_path)
file_id = ret['id']
```

#### Creating Knowledge Collection
```
def create_knowledge(token):
    url = f'http://localhost:8080/api/v1/knowledge/create'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    data = {
        'name': 'KB_name',
        'description': 'KB desc'
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

ret = create_knowledge(token)
knowledge_id = ret['id']
```

#### Adding Files to Knowledge Collections
```
def add_file_to_knowledge(token, knowledge_id, file_id):
    url = f'http://localhost:8080/api/v1/knowledge/{knowledge_id}/file/add'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    data = {'file_id': file_id}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

ret = add_file_to_knowledge(token, knowledge_id, file_id)
```

#### Using Files and Collections in Chat Completions
##### Using an Individual File in Chat Completions
```
def chat_with_file(token, model, query, file_id):
    url = 'http://localhost:8080/api/chat/completions'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    payload = {
        'model': model,
        'messages': [{'role': 'user', 'content': query}],
        'files': [{'type': 'file', 'id': file_id}]
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

query = f'*** Custom query based on the local file ***'
ret = chat_with_file(token, model, query, file_id)
print(f'{ret["choices"][0]["message"]["content"]}')
```

##### Using a Knowledge Collection in Chat Completions
```
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

ret = chat_with_collection(token, model, query, knowledge_id)
print(f'{ret["choices"][0]["message"]["content"]}')
```

### More Examples
Refer this [link](https://docs.openwebui.com/getting-started/advanced-topics/api-endpoints) for more examples
