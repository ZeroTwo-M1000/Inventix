import jwt
from fastapi import Depends, Request
from jwt import PyJWTError

from api.user.dao import UserDAO
from core.config import settings
from exception.TokenError import NotAuthorizedError, TokenError


def get_token(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise NotAuthorizedError
    return token


async def get_current_user(token=Depends(get_token)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except PyJWTError:
        raise TokenError
    name = payload.get("sub")
    if not name:
        raise TokenError
    user = await UserDAO.get_by_name(name)
    if not user:
        raise TokenError
    return user
