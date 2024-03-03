from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "user" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "hashed_password" VARCHAR(1024) NOT NULL,
    "is_active" INT NOT NULL  DEFAULT 1,
    "is_superuser" INT NOT NULL  DEFAULT 0,
    "is_verified" INT NOT NULL  DEFAULT 0
);
CREATE INDEX IF NOT EXISTS "idx_user_email_1b4f1c" ON "user" ("email");
CREATE TABLE IF NOT EXISTS "bunny" (
    "tg_id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "invited" INT,
    "coins" INT NOT NULL  DEFAULT 0,
    "productivity" INT NOT NULL  DEFAULT 1,
    "experience" INT NOT NULL,
    "endurance" INT NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
