from pydantic import BaseModel, field_validator
from typing import List
from datetime import datetime
from services.commons.model import Meta


class ReviewModel(BaseModel):
    body: str
    score: int
    title: str
    user_uuid: str
    created_at: datetime
    updated_at: datetime
    uuid: str

    @field_validator("uuid", "user_uuid", "created_at", "title", "score", "updated_at", "body")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field must not be empty")
        else:
            return value


class ReviewsModel(BaseModel):
    mete: Meta
    reviews: List[ReviewModel]

    @field_validator("reviews", "meta", check_fields=False)
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field must not be empty")
        else:
            return value