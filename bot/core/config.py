from __future__ import annotations
from pathlib import Path
from typing import TYPE_CHECKING

from pydantic_settings import BaseSettings, SettingsConfigDict

if TYPE_CHECKING:
    from sqlalchemy.engine.url import URL

DIR = Path(__file__).absolute().parent.parent.parent
BOT_DIR = Path(__file__).absolute().parent.parent


class EnvBaseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


class WebhookSettings(EnvBaseSettings):
    USE_WEBHOOK: bool
    WEBHOOK_BASE_URL: str
    WEBHOOK_PATH: str 
    WEBHOOK_SECRET: str 
    WEBHOOK_HOST: str
    WEBHOOK_PORT: int = 8080

    @property
    def webhook_url(self) -> str:
        if settings.USE_WEBHOOK:
            return f"{self.WEBHOOK_BASE_URL}{self.WEBHOOK_PATH}"
        return f"http://localhost:{settings.WEBHOOK_PORT}{settings.WEBHOOK_PATH}"


class BotSettings(WebhookSettings):
    BOT_TOKEN: str


class DBSettings(EnvBaseSettings):
    DB_HOST: str = "postgres"
    DB_PORT: int = 5432
    DB_USER: str = "postgres"
    DB_PASS: str | None = None
    DB_NAME: str = "postgres"

    @property
    def database_url(self) -> URL | str:
        if self.DB_PASS:
            return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return f"postgresql+asyncpg://{self.DB_USER}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def database_url_psycopg2(self) -> str:
        if self.DB_PASS:
            return f"postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return f"postgresql://{self.DB_USER}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


class CacheSettings(EnvBaseSettings):
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_PASSWORD: str | None = None
    REDIS_USER: str | None = None

    # REDIS_DATABASE: int = 1
    # REDIS_TTL_STATE: int | None = None
    # REDIS_TTL_DATA: int | None = None

    @property
    def redis_url(self) -> str:
        if self.REDIS_PASSWORD:
            return f"redis://{self.REDIS_USER}:{self.REDIS_PASSWORD}@{self.REDIS_HOST}:{self.REDIS_PORT}/0"
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/0"



class ApiSettings(EnvBaseSettings):
    API_URL: str = "http://localhost:8000"
    API_STATS_PATH: str
    API_MAIN_STATS_PATH: str



class Settings(BotSettings, DBSettings, CacheSettings, ApiSettings):
    DEBUG: bool = False

    SENTRY_DSN: str | None = None




settings = Settings()
