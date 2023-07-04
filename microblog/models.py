from core.db import Base
from sqlalchemy import Column, String, Integer, VARCHAR, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime


class Post(Base):
    __tablename__ = "microblog_posts"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(VARCHAR(350))
    date = Column(DateTime, default=datetime.utcnow)
    user = Column(UUID(as_uuid=True), ForeignKey('user.id'))
