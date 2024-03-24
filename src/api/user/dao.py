from api.user.schemas import SUser, SUserCreate, SUserMe
from core.config import settings


class UserDAO:
    @staticmethod
    async def get_all() -> list[SUser]:
        users = await settings.prisma_connection.prisma.user.find_many()
        return [SUser(**user.dict()) for user in users]

    @staticmethod
    async def get_by_name(name: str):
        return await settings.prisma_connection.prisma.user.find_first(where={"name": name})

    @staticmethod
    async def create(user: SUserCreate):
        return await settings.prisma_connection.prisma.user.create(data=user.model_dump())

    @staticmethod
    async def get_me(user):
        return SUserMe(**user.dict())
