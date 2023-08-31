from fastapi import Request, APIRouter, Depends, Form, responses, status
from fastapi.responses import RedirectResponse
from models.user import User
from db.session import get_db
from sqlalchemy.orm import Session
from core.auth import create_access_token
from core import global_vars
from view.endpoints.movie import get_current_user_from_cookie

router = APIRouter()


@router.get('/login')
def login(req: Request, db: Session = Depends(get_db)):
    flash_message = global_vars.message
    global_vars.message = ''
    user = db.query(User).first()
    return req.app.state.views.TemplateResponse("login.html", {
        "request": req,
        "user": user,
        "flash_message": flash_message
    })


@router.post('/login')
def login(req: Request, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    if not username or not password:
        global_vars.message = '用户名和密码不能为空'
        return RedirectResponse(url="/login", status_code=303)
    else:
        user = db.query(User).filter(User.username == username).first()
        if user and user.validate_password(password):
            global_vars.message = '登录成功'
            jwt_token = create_access_token(data={'username': username})
            response = responses.RedirectResponse("/", status_code=status.HTTP_302_FOUND)
            response.set_cookie(key="access_token", value=f"{jwt_token}", httponly=True)
            return response
        else:
            global_vars.message = '用户名或密码错误'
            return RedirectResponse(url="/login", status_code=303)


@router.get('/logout')
def logout():
    global_vars.message = '退出登录,bye bye!'
    response = responses.RedirectResponse("/", status_code=status.HTTP_302_FOUND)
    response.delete_cookie("access_token")
    return response


@router.get('/settings')
def settings(req: Request, current_user: dict = Depends(get_current_user_from_cookie)):
    return req.app.state.views.TemplateResponse("settings.html", {
        "request": req,
        "user": current_user,
        "is_authenticated": current_user['is_authenticated'],
    })


@router.post('/settings')
def settings(req: Request, name: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(User).first()
    user.name = name
    db.commit()
    global_vars.message = '用户名修改成功'
    # 使用重定向跳转回首页
    return RedirectResponse(url="/", status_code=303)
