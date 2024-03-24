from pydantic_settings import BaseSettings

from core.db import PrismaConnection
from utils.decorators import Decorators


class Settings(BaseSettings):
    prisma_connection: PrismaConnection = PrismaConnection()
    DATABASE_URL: str
    decorators: Decorators = Decorators()

    SECRET_KEY: str
    ALGORITHM: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
