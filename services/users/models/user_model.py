from pydantic import BaseModel, field_validator
from typing import List
from services.commons.model import Meta


class UserModel(BaseModel):
    avatar_url: str
    email: str
    name: str
    nickname: str
    uuid: str


    @field_validator("email", "name", "nickname", "uuid", "avatar_url")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field must not be empty")
        else:
            return value


class UsersModel(BaseModel):
    meta: Meta
    users: List[UserModel]

