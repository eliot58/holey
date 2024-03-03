from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config.settings import DATABASE_URI, APPS_MODELS
from src.auth.config import auth_backend, fastapi_users
from src.bunny.router import router as router_bunny
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI(
    title="Holey"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(router_bunny)


origins = ['*']
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)


register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": APPS_MODELS},
    generate_schemas=True,
    add_exception_handlers=True,
)