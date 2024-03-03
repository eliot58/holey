from fastapi_users.authentication import BearerTransport
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)
from fastapi_users import FastAPIUsers
from src.auth.manager import get_user_manager
from src.config.settings import SECRET_AUTH
from src.auth.models import User

bearer_transport = BearerTransport(tokenUrl="auth/login")

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET_AUTH, lifetime_seconds=60 * 10)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend]
)

current_user = fastapi_users.current_user(active=True, verified=True)