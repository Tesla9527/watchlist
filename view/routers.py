"""
视图路由
"""
from fastapi import APIRouter
from view.endpoints import movie

view_router = APIRouter()
view_router.include_router(movie.router, prefix='', tags=["电影管理"])
