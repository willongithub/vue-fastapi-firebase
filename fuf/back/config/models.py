from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str
    tag: str


class UserBase(BaseModel):
    username: str
    email: str
    full_name: str = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str
