from typing import List
from fastapi import APIRouter
from . import service
from .schemas import PostCreate, PostList
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.db import get_async_session

router = APIRouter()


@router.get("/", response_model=List[PostList])
async def post_list(session: AsyncSession = Depends(get_async_session)):
    return await service.get_post_list(session)


@router.post("/")
async def post_list(item: PostCreate, session: AsyncSession = Depends(get_async_session)):
    return await service.create_post_(session, item)
