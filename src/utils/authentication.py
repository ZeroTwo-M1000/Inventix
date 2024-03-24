from datetime import datetime, timedelta

import jwt
from passlib.context import CryptContext

from api.user.dao import UserDAO
from core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, settings.ALGORITHM
    )
    return encoded_jwt


async def authenticate_user(name: str, password: str):
    user = await UserDAO.get_by_name(name)
    if not user:
        return False
    if not verify_password(password, user.hash_password):
        return False
    return user
