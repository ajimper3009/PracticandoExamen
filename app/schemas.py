from pydantic import BaseModel, EmailStr
from pydantic import ConfigDict
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)  # ✅ Nueva forma en Pydantic v2
    # class Config:
    #     # orm_mode = True
    #     from_attributes = True  # <- Nueva forma en Pydantic v2 

