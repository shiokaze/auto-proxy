import json

import openai
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/chat")
def chat(message):
    print("msg received")
    rsp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message
    )
    try:
        print("proxy rsp" + json.dumps(rsp))
    except Exception:
        print(Exception)
    return rsp



