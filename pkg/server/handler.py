import json

import openai
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pkg.server.log import get_logger

log = get_logger(__name__)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class GBTForwardReq(BaseModel):
    message: list


@app.post("/chat")
def chat(req: GBTForwardReq):
    log.info("proxy req" + json.dumps(req, ensure_ascii=False))
    rsp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=req.message
    )
    log.info("proxy rsp" + json.dumps(rsp, ensure_ascii=False))
    return rsp
