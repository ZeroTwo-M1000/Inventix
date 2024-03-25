from fastapi import APIRouter, HTTPException

from api.review.dao import ParserDao
from api.review.schemas import SReviewParse, SReviewCreate
from api.site.dao import SiteDAO

router = APIRouter()


@router.post("")
async def create_review(data: SReviewParse):
    site = await SiteDAO.get_by_name(data.Site)
    if not site:
        raise HTTPException(status_code=404, detail="Site not found")
    review = SReviewCreate(**data.dict(exclude={"Site"}), siteId=site.id)
    await ParserDao.create(review)
