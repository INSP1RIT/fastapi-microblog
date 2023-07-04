from .models import Post
from .schemas import PostCreate

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


async def get_post_list(session: AsyncSession):
    res = await session.execute(select(Post))
    return res.scalars().all()


async def create_post_(session: AsyncSession, item: PostCreate):
    post = Post(**item.dict())
    session.add(post)
    await session.commit()
    await session.refresh(post)
    return post
