from fastapi import Request, APIRouter, Depends
from fastapi.responses import HTMLResponse
from models.movie import Movie
from db.session import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def index(request: Request, db: Session = Depends(get_db)):
    """
    首页
    :param db:
    :param request:
    :return:
    """
    name = 'Tesla Lau'
    movies = db.query(Movie).all()
    return request.app.state.views.TemplateResponse("index.html", {"request": request, "name": name, "movies": movies})
