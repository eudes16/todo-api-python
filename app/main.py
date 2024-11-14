import os
from dotenv import load_dotenv
from fastapi import Depends, FastAPI

from app.http.middleware.request_process_middleware import RequestProcessMiddleware


load_dotenv()


from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import items, users

app = FastAPI(
    
    # dependencies=[Depends(get_query_token)]
)

app.add_middleware(RequestProcessMiddleware)
app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    app_name = os.getenv("APP_NAME")

    return {
        "app_name": app_name,
        "message": "Welcome to this fantastic app!",
        "version": "0.0.1",
    }