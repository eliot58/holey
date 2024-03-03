from fastapi_users_tortoise import TortoiseUserDatabase
from src.auth.models import User


async def get_user_db():
    yield TortoiseUserDatabase(User)