from typing import Any, Dict, Optional, List

from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int

    TELEGRAM_BOT_TOKEN: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()
