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
    rsp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message
    )
    return rsp



