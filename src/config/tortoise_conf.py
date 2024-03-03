from src.config.settings import DATABASE_URI, APPS_MODELS

TORTOISE_ORM = {
    "connections": {"default": "sqlite://db.sqlite3"},
    "apps": {
        "models": {
            "models": APPS_MODELS,
            "default_connection": "default",
        }
    },
}