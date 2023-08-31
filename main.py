from fastapi import FastAPI, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from core.config import settings
from view.routers import view_router
from core import events, exceptions

# FastAPI实例
app = FastAPI(
    debug=settings.APP_DEBUG,
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

# 事件监听
app.add_event_handler("startup", events.startup(app))
app.add_event_handler("shutdown", events.stopping(app))

# 异常错误处理
app.add_exception_handler(404, exceptions.http_exception_handel)
app.add_exception_handler(400, exceptions.http_exception_handel)
app.add_exception_handler(500, exceptions.http_exception_handel)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 添加路由
app.include_router(view_router)

# 静态资源目录
app.mount('/static', StaticFiles(directory=settings.STATIC_DIR), name="static")
app.state.views = Jinja2Templates(directory=settings.TEMPLATE_DIR)

# 启动
if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, port=9527)
