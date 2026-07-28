from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI(
    title="1",
    description="1",
    version="1",
)

class User(BaseModel):
    name:str
    age:int
    pwd:str | None
    sex:str = '男'

@app.post('/users/')
def create_user(user: User):
    return user

# @app.post('/users/')
# def create_user(user: dict):
#     return user


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("url_post_01:app", host="0.0.0.0", port=8000, reload=True)

