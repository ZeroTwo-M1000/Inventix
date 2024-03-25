from api.review.schemas import SReviewCreate
from core.config import settings


class ParserDao:
    @staticmethod
    async def create(review: SReviewCreate):
        if await settings.prisma_connection.prisma.review.find_first(where={"text": review.text}):
            return

        await settings.prisma_connection.prisma.review.create(data=review.model_dump())
