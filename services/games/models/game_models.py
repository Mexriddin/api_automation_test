from pydantic import BaseModel, field_validator
from typing import List
from services.commons.model import Meta



class GameModel(BaseModel):
    title: str
    uuid: str


    @field_validator("title", "uuid")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field must not be empty")
        else:
            return value


class GamesModel(BaseModel):
    items: List[GameModel]
    meta: Meta

