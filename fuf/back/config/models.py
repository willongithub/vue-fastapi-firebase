from enum import Enum

from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str
    tag: str


class UserType(str, Enum):
    admin = "admin"
    coordinator = "coordinator"
    participant = "participant"


class UserBase(BaseModel):
    username: str
    group: str | None = None
    type: UserType | None = UserType.participant
    active: bool | None = True


class UserIn(UserBase):
    password: str


class User(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
