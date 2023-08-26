import os
from dotenv import load_dotenv, find_dotenv
from pydantic_settings import BaseSettings
from typing import List
import os


class Config(BaseSettings):
    # 加载环境变量
    load_dotenv(find_dotenv(), override=True)
    # 调试模式
    APP_DEBUG: bool = True
    # 项目信息
    VERSION: str = "0.0.1"
    PROJECT_NAME: str = "watchlist"
    DESCRIPTION: str = '<a href="/redoc" target="_blank">redoc</a>'
    # 静态资源目录
    STATIC_DIR: str = os.path.join(os.getcwd(), "static")
    TEMPLATE_DIR: str = os.path.join(STATIC_DIR, "templates")

    # 数据库地址
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./db/test.db"


settings = Config()
