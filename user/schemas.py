import uuid
from typing import Optional

from fastapi_users import schemas, models
from pydantic import EmailStr
from datetime import date


class UserRead(schemas.BaseUser[uuid.UUID]):
    id: models.ID
    email: EmailStr
    name: str
    date: date
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    email: EmailStr
    password: str
    name: str
    date: date
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    password: Optional[str]
    email: Optional[EmailStr]
    name: Optional[str]
    is_active: Optional[bool]
    is_superuser: Optional[bool]
    is_verified: Optional[bool]
