from fastapi import Request, APIRouter, Depends, Form, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from models.user import User
from db.session import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.get('/login')
def login(req: Request):
    user = {'name': 'Tesla Lau'}
    return req.app.state.views.TemplateResponse("login.html", {"request": req, "user": user})


@router.post('/login')
def login(req: Request, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    username = username
    password = password
    if not username or not password:
        print('用户名和密码不能为空')
        return RedirectResponse(url="/", status_code=303)
    else:
        user = db.query(User).filter(User.name == username).first()
        if user and user.validate_password(password):
            return RedirectResponse(url="/", status_code=303)
        else:
            print('用户名和密码错误')
            return RedirectResponse(url="/", status_code=303)
