from fastapi import FastAPI
import uvicorn
from config import settings
from api.api import api_router

# FastAPI实例
app = FastAPI(
    debug=settings.APP_DEBUG,
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

# 添加路由
app.include_router(api_router)

# 启动
if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, port=9527)
