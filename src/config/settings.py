import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URI = f'postgres://{os.environ.get("DB_USER")}:' \
               f'{os.environ.get("DB_PASS")}@' \
               f'{os.environ.get("DB_HOST")}:5432/' \
               f'{os.environ.get("DB_NAME")}'

SECRET_AUTH = os.environ.get("SECRET_AUTH")

# DB_HOST_TEST = os.environ.get("DB_HOST_TEST")
# DB_PORT_TEST = os.environ.get("DB_PORT_TEST")
# DB_NAME_TEST = os.environ.get("DB_NAME_TEST")
# DB_USER_TEST = os.environ.get("DB_USER_TEST")
# DB_PASS_TEST = os.environ.get("DB_PASS_TEST")

APPS_MODELS = [
    "src.auth.models",
    "src.bunny.models",
    "aerich.models",
]