from fastapi import APIRouter, HTTPException

from api.site.dao import SiteDAO
from api.site_data.dao import SiteDataDAO
from api.site_data.schemas import SBaseSiteDataCreate, SBaseSiteDataParse
from core.config import settings

router = APIRouter()


@router.post("")
async def create(data: SBaseSiteDataParse, name: str):
    site = await SiteDAO.get_by_name(name)
    reviews_len = await settings.prisma_connection.prisma.review.count(where={"siteId": site.id})
    count_bad_review = await settings.prisma_connection.prisma.review.count(
        where={
            "siteId": site.id,
            "bad_text": {"not": None},
        }
    )
    count_good_review = await settings.prisma_connection.prisma.review.count(
        where={
            "siteId": site.id,
            "good_text": {"not": None},
        }
    )
    if not site:
        raise HTTPException(status_code=404, detail="Site not found")
    return await SiteDataDAO.create(
        SBaseSiteDataCreate(
            siteId=site.id,
            count_review=reviews_len,
            count_bad_review=count_bad_review,
            count_good_review=count_good_review,
            **data.dict(),
        )
    )
