from fastapi import APIRouter

from api.review.crud import router as review_router
from api.site.crud import router as site_router
from api.user.crud import router as user_router

api_router = APIRouter()

api_router.include_router(user_router, prefix="/user", tags=["Users"])
api_router.include_router(review_router, prefix="/review", tags=["Reviews"])
api_router.include_router(site_router, prefix="/site", tags=["Sites"])
