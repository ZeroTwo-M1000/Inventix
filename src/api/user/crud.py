from fastapi import APIRouter, Depends, HTTPException, Response

from api.user.dao import UserDAO
from api.user.schemas import SUser, SUserCreate, SUserLogin
from utils.authentication import authenticate_user, create_access_token, get_password_hash
from utils.depends import get_current_user

router = APIRouter()


@router.get("/all")
async def get_all_users(token=Depends(get_current_user)) -> list[SUser]:
    return await UserDAO.get_all()


@router.post("/login")
async def login(response: Response, user: SUserLogin) -> dict:
    user_db = await UserDAO.get_by_name(user.name)
    if not user_db or not await authenticate_user(user.name, user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = create_access_token(data={"sub": user.name})
    response.set_cookie(key="access_token", value=token, httponly=True)
    return {"details": "Login successful"}


@router.post("/register")
async def register(response: Response, user: SUserCreate):
    if await UserDAO.get_by_name(user.name):
        raise HTTPException(status_code=400, detail="User already exists")

    user.hash_password = get_password_hash(user.hash_password)
    await UserDAO.create(user)

    response.set_cookie(key="access_token", value=create_access_token(data={"sub": user.name}))
    return {"details": "Register successful"}


@router.get("/me")
async def get_me(token=Depends(get_current_user)):
    return await UserDAO.get_me(token)
