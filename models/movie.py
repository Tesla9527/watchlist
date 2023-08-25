from sqlalchemy import Column, Integer, String
from db.base_class import Base


class Movie(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(60))
    year = Column(String(4))
