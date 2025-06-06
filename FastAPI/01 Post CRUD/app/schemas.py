from pydantic import BaseModel, EmailStr
from datetime import datetime

class PostBase(BaseModel):
    title: str
    description: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime

class User(BaseModel):
    email: EmailStr
    password: str

class UserOut(User):
    id: int
    created_at: datetime
