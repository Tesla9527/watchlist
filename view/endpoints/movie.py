from fastapi import Request, APIRouter, Depends, Form, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from models.movie import Movie
from models.user import User
from db.session import get_db
from sqlalchemy.orm import Session
from core.auth import decode_access_token

router = APIRouter()


# 解密 JWT 令牌并获取用户数据
def get_current_user_from_cookie(request: Request):
    token = request.cookies.get("access_token")
    if token is None:
        return False
    user_data = decode_access_token(token)['name']
    return True


@router.get("/", response_class=HTMLResponse)
async def index(req: Request, current_user: dict = Depends(get_current_user_from_cookie)
                , db: Session = Depends(get_db)):
    is_authenticated = current_user

    user = db.query(User).first()
    movies = db.query(Movie).all()
    return req.app.state.views.TemplateResponse("index.html", {"request": req, "user": user, "movies": movies,
                                                               "is_authenticated": is_authenticated})


@router.post("/movies/create/")
async def create(title: str = Form(...), year: int = Form(...), db: Session = Depends(get_db)):
    new_movie = Movie(title=title, year=year)
    db.add(new_movie)
    db.commit()
    # 使用重定向跳转回首页
    return RedirectResponse(url="/", status_code=303)


@router.get("/movies/{movie_id}/edit/", response_class=HTMLResponse)
async def edit_movie_page(req: Request, movie_id: int, db: Session = Depends(get_db)):
    user = db.query(User).first()
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
