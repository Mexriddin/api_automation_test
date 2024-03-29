from pydantic import BaseModel, field_validator
from typing import List
from services.games.models.game_models import GameModel


class WishlistsModel(BaseModel):
    items: List[GameModel]
    user_uuid: str


    @field_validator("items", "user_uuid")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field must not be empty")
        else:
            return value


class ErrorModel(BaseModel):
    message: str
    code: int

    @field_validator("code", "message")
    def field_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field must not be empty")
        else:
            return value