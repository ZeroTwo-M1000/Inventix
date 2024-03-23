from pydantic_settings import BaseSettings
from core.db import PrismaConnection


class Settings(BaseSettings):
    prisma_connection: PrismaConnection = PrismaConnection()
    DATABASE_URL: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
