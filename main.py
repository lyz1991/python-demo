from fastapi import FastAPI, Form
import uvicorn as uvicorn
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
app = FastAPI()


origins = [
    "http://localhost:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Item(BaseModel):
    name: str

@app.get('/items/{item_id}')
def items(item_id: int, day: str = None):
    return {'message': '欢来到接口页面'}

@app.post('/log')
def getLog(data: str=Form(...)):
    return {'message': '欢来到接口页面'}

if __name__ == '__main__':
    uvicorn.run('main:app', host="127.0.0.1", port=8080, reload=True)