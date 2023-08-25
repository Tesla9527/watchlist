from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from core.config import settings

# 创建一个数据库引擎，用于连接到 SQLite 数据库
engine = create_engine(settings.SQLALCHEMY_DATABASE_URL)

# 创建一个会话生成器，用于生成数据库会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建一个 SQLAlchemy 的基类，用于定义数据库模型类
Base = declarative_base()


def get_db():
    """
    获取数据库会话的上下文管理器
    """
    db = SessionLocal()
    try:
        yield db  # 返回数据库会话供函数使用
    finally:
        db.close()  # 在使用后关闭会话
