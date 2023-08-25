from fastapi import APIRouter
from schemas.movie import MovieResponse, MovieCreate, MovieUpdate

router = APIRouter()


@router.post("/movies/", response_model=MovieResponse)
async def create_movie(movie: MovieCreate):
    return movie


@router.get("/movies/{movie_id}", response_model=MovieResponse)
async def read_movie(movie_id: int):
    return {"id": movie_id}


@router.put("/movies/{movie_id}", response_model=MovieResponse)
async def update_movie(movie_id: int, movie: MovieUpdate):
    return {"id": movie_id, **movie.dict()}


@router.delete("/movies/{movie_id}", response_model=dict)
async def delete_movie(movie_id: int):
    return {"message": f"Movie {movie_id} has been deleted"}
