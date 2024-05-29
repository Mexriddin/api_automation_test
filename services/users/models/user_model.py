from pydantic import BaseModel, field_validator, Field, EmailStr
from typing import List
from services.commons.model import Meta


class UserModel(BaseModel):
    avatar_url: str
    email: EmailStr = Field(..., min_length=5, max_length=100,
                            pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    name: str = Field(..., min_length=1, max_length=100, pattern=r"^\S.+$")
    nickname: str = Field(..., min_length=2, max_length=200, pattern=r"^[a-zA-Z0-9_.+-]+$")
    uuid: str = Field(..., min_length=36, max_length=36,
                      pattern=r'[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-['
                              r'a-fA-F0-9]{12}')

    @field_validator("email", "name", "nickname", "uuid")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field must not be empty")
        else:
            return value


class UsersModel(BaseModel):
    meta: Meta
    users: List[UserModel]

    @field_validator("users", "meta")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field must not be empty")
        else:
            return value