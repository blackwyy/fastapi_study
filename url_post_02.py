from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI(
    title='post查询',
    description='post查询2',
    version='1.0'
)

class Car(BaseModel):
    name:str
    price:int = 1


@app.post('/createCar')
def createCar(car: Car):
    return car

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("url_post_02:app", host='0.0.0.0', port=8001, reload=True)