from pydantic import BaseModel, field_validator
from typing import List


class UserModel(BaseModel):
    email: str
    name: str
    nickname: str
    uuid: str


    @field_validator("email", "name", "nickname", "uuid")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field must not be empty")
        else:
            return value


class Meta(BaseModel):
    total: int

    @field_validator("total")
    def field_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field must not be empty")
        else:
            return value


class UsersModel(BaseModel):
    items: List[UserModel]
    meta: Meta