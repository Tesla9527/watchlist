from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/", tags=["门户首页"], response_class=HTMLResponse)
async def home(request: Request):
    """
    门户首页
    :param request:
    :return:
    """
    name = 'Grey Li'
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]
    return request.app.state.views.TemplateResponse("index.html", {"request": request, "name": name, "movies": movies})
