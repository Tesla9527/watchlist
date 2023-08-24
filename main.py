from fastapi import FastAPI
import uvicorn
from config import settings

app = FastAPI(
    debug=settings.APP_DEBUG,
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)


@app.get('/')
def index():
    return 'are you ok?'


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, port=9527)
