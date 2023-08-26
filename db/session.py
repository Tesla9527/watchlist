from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings

# 创建一个数据库引擎，用于连接到数据库
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}, pool_pre_ping=True)

# 创建一个会话生成器，用于生成数据库会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# 创建数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
