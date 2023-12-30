from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    ...

class User(BaseModel):
    id: int
    username: str
    email: str
    
    class Config:
        from_attributes = True



