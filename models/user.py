from sqlalchemy import Column, Integer, String
from db.base_class import Base
from werkzeug.security import generate_password_hash, check_password_hash


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))  # 展示用
    username = Column(String(20))  # 账号
    password_hash = Column(String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)
