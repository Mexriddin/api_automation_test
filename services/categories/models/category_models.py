from pydantic import BaseModel, field_validator, Field
from typing import List
from services.commons.model import Meta


class CategoryModel(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    uuid: str = Field(..., min_length=36, max_length=36,
                      pattern=r'[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-['
                              r'a-fA-F0-9]{12}')

    @field_validator("name", "uuid")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field must not be empty")
        else:
            return value


class CategoriesModel(BaseModel):
    categories: List[CategoryModel]
    meta: Meta

    @field_validator("categories", "meta")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field must not be empty")
        else:
            return value