import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import openai

load_dotenv()

app = FastAPI()



class Data(BaseModel):
    text: str


@app.post("/summarize")
async def summarize(data: Data):
    openai.organization = os.environ.get('OPENAI_ORGANIZATION', None)
    openai.api_key = os.environ.get('OPENAI_API_KEY', None)
    engine_list = openai.Engine.list()
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{data.text}\nTl;dr",
        temperature=0.7,
        max_tokens=140,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0,
        stop=["\n"]
    )
    return {
        "summary": response["choices"][0]["text"]
    }