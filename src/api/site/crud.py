from fastapi import APIRouter

from api.site.dao import SiteDAO

router = APIRouter()


@router.get("/")
async def get_all():
    return await SiteDAO.get_all()


@router.get("/{name}")
async def get_by_name(name: str):
    return await SiteDAO.get_by_name(name)


@router.get("/{name}/full")
async def get_by_name(name: str):
    return await SiteDAO.get_by_name_full(name)
