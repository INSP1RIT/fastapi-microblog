from core import Base
from core.db import get_async_session
from sqlalchemy import Column, VARCHAR, Integer, DateTime, String, Boolean
from datetime import datetime
from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "user"

    name = Column(VARCHAR(50), unique=True)
    date = Column(DateTime, default=datetime.utcnow)


def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
