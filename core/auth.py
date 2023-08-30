"""
JWT鉴权
"""

from datetime import timedelta, datetime
import jwt
from fastapi import HTTPException
from core.config import settings


def create_access_token(data: dict):
    """
    创建token
    :param data: 加密数据
    :return: jwt
    """
    token_data = data.copy()
    # token超时时间
    expire = datetime.utcnow() + timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
    # 向jwt加入超时时间
    token_data.update({"exp": expire})
    # jwt加密
    jwt_token = jwt.encode(token_data, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

    return jwt_token


def decode_access_token(token: str):
    try:
        decoded_data = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        return decoded_data
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.DecodeError:
        raise HTTPException(status_code=401, detail="Token decoding failed")
