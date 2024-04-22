from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import os, requests, uvicorn

class CompletionItem(BaseModel):
    prompt: str

class EmbeddingItem(BaseModel):
    content: str

class TokenizeItem(BaseModel):
    content: str

class DetokenizeItem(BaseModel):
    tokens: list[int]

description = 'App description'

app = FastAPI(
    title="Llama.cpp App",
    description=description,
    summary='App summary',
    version='0.0.1',
    terms_of_service='App terms of service',
    contact={
        'name': 'Support',
        'url': 'http://www.contacturl.com',
        'email': 'contact@email.com',
    },
    license_info={
        'name': 'Apache License 2.0',
        'identifier': 'Apache-2.0'
    },
)

base_url = 'http://localhost:8080'

@app.get("/health")
async def health():
    url = f'{base_url}/health'
    r = requests.get(url)
    return r.json()

@app.get("/props")
async def props():
    url = f'{base_url}/props'
    r = requests.get(url)
    return r.json()

@app.get("/slots")
async def slots():
    url = f'{base_url}/slots'
    r = requests.get(url)
    return r.json()

@app.post("/tokenize")
async def tokenize(item: TokenizeItem):
    payload = jsonable_encoder(item)
    url = f'{base_url}/tokenize'
    r = requests.post(url, json=payload)

    return r.json()

@app.post("/detokenize")
async def detokenize(item: DetokenizeItem):
    payload = jsonable_encoder(item)
    url = f'{base_url}/detokenize'
    r = requests.post(url, json=payload)

    return r.json()

@app.post("/embedding")
async def embedding(item: EmbeddingItem):
    payload = jsonable_encoder(item)
    url = f'{base_url}/embedding'
    r = requests.post(url, json=payload)

    return r.json()

@app.post("/completion")
async def completion(item: CompletionItem):
    payload = jsonable_encoder(item)
    url = f'{base_url}/completion'
    r = requests.post(url, json=payload)

    """
    import json
    with open("payload.json", "r") as f:
        my_dict = json.load(f)
    print(f'+++ data: {my_dict}')

    #r = requests.post(url, json=payload)
    headers = {"Content-type": "application/json"}

    r = requests.post(url, json=my_dict, headers=headers)
    """

    return r.json()


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=int(os.getenv('APP_PORT')))
