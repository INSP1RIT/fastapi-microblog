from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    text: str

    class Config:
        orm_mode = True


class PostList(PostBase):
    id: int


class PostCreate(PostBase):
    pass
