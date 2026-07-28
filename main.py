from fastapi import FastAPI

app = FastAPI(
    title="Fastapi 学习的后端系统",
    description="基于 FastAPI 的徐子",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "fastapi study 系统运行正常"}


# 命令行启动虚拟任务
# uvicorn url_post_01:app --host 0.0.0.0 --port 8000 --reload