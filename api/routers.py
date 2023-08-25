"""
api路由
"""
from fastapi import APIRouter
from api.endpoints import movie

api_router = APIRouter()
api_router.include_router(movie.router, prefix='/movie', tags=["电影管理"])
