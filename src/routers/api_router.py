from api.user.crud import router as user_router
from fastapi import APIRouter, Response

api_router = APIRouter()
api_router.include_router(user_router, prefix="/user", tags=["Users"])
