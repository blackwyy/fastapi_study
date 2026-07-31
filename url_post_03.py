from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Union, Optional

app=FastAPI(
    title='test3',
    description='test3',
    version='1.0'
)

class Persion(BaseModel):
    name:str | None
    age:int
    sex:str = '男'

@app.post('/createPersion')
def createPersion(persion: Persion):
    return persion


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('url_post_03:app', host='0.0.0.0', port=8000, reload=True)
