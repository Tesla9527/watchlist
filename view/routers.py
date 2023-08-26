"""
视图路由
"""
from fastapi import APIRouter
from view.endpoints import movie, login

view_router = APIRouter()
view_router.include_router(movie.router, prefix='', tags=["电影管理"])
view_router.include_router(login.router, prefix='', tags=["登录管理"])
