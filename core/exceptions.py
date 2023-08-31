from fastapi import Request
from fastapi.exceptions import HTTPException


def http_exception_handel(req: Request, exc: HTTPException):
    user = {'name': 'no name'}
    if exc.status_code == 404:
        return req.app.state.views.TemplateResponse("/errors/404.html", {"request": req, "user": user})

    if exc.status_code == 400:
        return req.app.state.views.TemplateResponse("/errors/400.html", {"request": req, "user": user})

    if exc.status_code == 500:
        return req.app.state.views.TemplateResponse("/errors/500.html", {"request": req, "user": user})
