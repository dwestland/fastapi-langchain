from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from pydantic import BaseModel
from app.api.api_v1.api import router as api_router

import os

from dotenv import load_dotenv  

load_dotenv()

chat_model = ChatOpenAI(model_name='gpt-3.5-turbo')

loader=PyPDFLoader('./Docs/ChatGPT_wikipedia.pdf')
index=VectorstoreIndexCreator().from_loaders([loader])

app=FastAPI()

# CORS
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"]
                   )

class Item(BaseModel):
    query:str

@app.get('/')
def read_root():
    return {"Hello": "world"}

@app.post('/')
def answer_query(item:Item):
    print(item)
    try:
        response=index.query(item.query)
        return response
    except:
        return {"message":"Some error happened"}


app.include_router(api_router, prefix="/api/v1")

