from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class SUser(BaseModel):
    id: str
    name: str
    hash_password: str
    role: str
    img: Optional[str] = None
    date: datetime


class SUserCreate(BaseModel):
    name: str
    hash_password: str
    role: str


class SUserLogin(BaseModel):
    name: str
    password: str


class SUserMe(BaseModel):
    name: str
    role: str
    img: Optional[str] = None
    date: datetime
