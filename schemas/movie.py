from pydantic import BaseModel
from typing import Optional


class MovieCreate(BaseModel):
    title: str
    year: int


class MovieUpdate(BaseModel):
    title: Optional[str] = None
    year: Optional[int] = None


class MovieResponse(MovieCreate):
    id: int
