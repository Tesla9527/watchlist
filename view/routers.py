"""
视图路由
"""
from fastapi import APIRouter
from view.endpoints import home

view_router = APIRouter()

view_router.include_router(home.router)
