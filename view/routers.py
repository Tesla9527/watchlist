"""
视图路由
"""
from fastapi import APIRouter
from view.endpoints import index

view_router = APIRouter()
view_router.include_router(index.router, prefix='', tags=["电影管理"])
