from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response

from core.db import session_local
from microblog.blog import router as blog_router

app = FastAPI()

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = session_local()
        response = await call_next(request)
    finally:
        request.state.db.close()

    return response

app.include_router(blog_router, prefix="/blog")




