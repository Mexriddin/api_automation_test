from pydantic import BaseModel, field_validator, Field
from typing import List
from datetime import datetime
from services.commons.model import Meta


class ReviewModel(BaseModel):
    body: str = Field(..., max_length=100, min_length=1)
    score: int = Field(..., ge=1, le=5)
    title: str = Field(..., max_length=100, min_length=1)
    user_uuid: str = Field(..., min_length=36, max_length=36,
                            pattern=r'[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-['
                                    r'a-fA-F0-9]{12}')
    created_at: datetime
    updated_at: datetime
    uuid: str = Field(..., min_length=36, max_length=36,
                            pattern=r'[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-['
                                    r'a-fA-F0-9]{12}')

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