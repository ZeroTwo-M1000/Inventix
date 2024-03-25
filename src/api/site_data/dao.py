from api.site_data.schemas import SBaseSiteDataCreate
from core.config import settings


class SiteDataDAO:

    @staticmethod
    async def create(data: SBaseSiteDataCreate):
        try:
            return await settings.prisma_connection.prisma.sitedata.create(data=data.model_dump())
        except:
            return
