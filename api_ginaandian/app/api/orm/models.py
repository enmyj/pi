from typing import Optional

from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    first_name: Optional[str]
    last_name: Optional[str]
    full_name: Optional[str]
    email: Optional[str]
    phone_number: Optional[str]
    zip_code: Optional[str]


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int


class UserUpdate(SQLModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    full_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    zip_code: Optional[str] = None
