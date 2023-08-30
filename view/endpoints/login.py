from fastapi import Request, APIRouter, Depends, Form, responses, status
from fastapi.responses import RedirectResponse
from models.user import User
from db.session import get_db
from sqlalchemy.orm import Session
from core.auth import create_access_token

router = APIRouter()


@router.get('/login')
def login(req: Request, db: Session = Depends(get_db)):
    user = db.query(User).first()
    return req.app.state.views.TemplateResponse("login.html", {"request": req, "user": user})


@router.post('/login')
def login(req: Request, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    if not username or not password:
        print('用户名和密码不能为空')
        return RedirectResponse(url="/login", status_code=303)
    else:
        user = db.query(User).filter(User.name == username).first()
        if user and user.validate_password(password):
            print('认证通过')
            jwt_token = create_access_token(data={'name': username})
            response = responses.RedirectResponse("/", status_code=status.HTTP_302_FOUND)
            response.set_cookie(key="access_token", value=f"{jwt_token}", httponly=True)
            return response
        else:
            print('用户名或密码错误')
            return RedirectResponse(url="/login", status_code=303)


@router.get('/logout')
def logout():
    print('退出登录,bye bye!')
    response = responses.RedirectResponse("/", status_code=status.HTTP_302_FOUND)
    response.delete_cookie("access_token")
    return response
