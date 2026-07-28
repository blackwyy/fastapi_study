from fastapi import FastAPI

app = FastAPI(
    title='这是一个测试的',
    description='这是一个测试的2',
    version='v1.10',
)

@app.get('/test01')
def test01():
    print('王洋测试使用')
    return {'result': '王洋测试使用'}

if __name__ == "__main__":
    import uvicorn
    print(f"__name__ = {__name__}")
    uvicorn.run(app, host="127.0.0.1", port=8001)

