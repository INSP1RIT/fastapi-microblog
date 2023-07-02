from core import Base
from sqlalchemy import Column, VARCHAR, Integer, DateTime, String, Boolean
from datetime import datetime


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(VARCHAR(50), unique=True)
    email = Column(VARCHAR(50), unique=True)
    password = Column(String)
    date = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
