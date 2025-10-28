import os

from pydantic_settings import BaseSettings
from pydantic import ConfigDict, Field, model_validator

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DATABASE_URL: str = Field(default_factory=lambda: "")

    SECRET_KEY: str
    ENCODE_ALGORYTHM: str

    model_config = ConfigDict(env_file=os.path.join(BASE_DIR, ".env"))

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     # вычисляем DATABASE_URL после инициализации всех полей
    #     self.DATABASE_URL = (
    #         f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    #     )

    @model_validator(mode="after")
    def build_database_url(self):
        self.DATABASE_URL = (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )
        return self

settings = Settings()
