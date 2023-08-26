from fastapi import Request, APIRouter, Depends, Form, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from models.movie import Movie
from db.session import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def index(req: Request, db: Session = Depends(get_db)):
    user = {'name': 'Tesla Lau'}
    movies = db.query(Movie).all()
    return req.app.state.views.TemplateResponse("index.html", {"request": req, "user": user, "movies": movies})


@router.post("/movies/create/")
async def create(title: str = Form(...), year: int = Form(...), db: Session = Depends(get_db)):
    new_movie = Movie(title=title, year=year)
    db.add(new_movie)
    db.commit()
    # 使用重定向跳转回首页
    return RedirectResponse(url="/", status_code=303)


@router.get("/movies/{movie_id}/edit/", response_class=HTMLResponse)
async def edit_movie_page(req: Request, movie_id: int, db: Session = Depends(get_db)):
    user = {'name': 'Tesla Lau'}
    movie = db.query(Movie).filter(Movie.id == movie_id).first()

    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    return req.app.state.views.TemplateResponse("edit.html", {"request": req, "user": user, "movie": movie})


@router.post("/movies/{movie_id}/edit/")
async def edit(movie_id: int, title: str = Form(...), year: int = Form(...),
               db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()

    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    movie.title = title
    movie.year = year
    db.commit()

    # 使用重定向跳转回首页
    return RedirectResponse(url="/", status_code=303)


@router.post("/movies/{movie_id}/delete/")
async def delete(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()

    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    db.delete(movie)
    db.commit()
    # 使用重定向跳转回首页
    return RedirectResponse(url="/", status_code=303)
