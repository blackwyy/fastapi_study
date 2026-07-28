# 路径参数使用
from fastapi import FastAPI

app=FastAPI(
    title='路径参数测试',
    description='路径参数测试',
    version='v1'
)

@app.get('/args/{id}/{name}')
def path_args(id:int,name):
    return {'ID':id,'Name':name}

@app.get('/query1')
def query1(page:int = 1,limit:int = 10):
    # if not page:
    #     page=1
    
    # if not limit:
    #     limit=10
    return {'page':page,'limit':limit}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("url_test_01:app", host="0.0.0.0", port=8000, reload=True)