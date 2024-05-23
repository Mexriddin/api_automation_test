from pydantic import BaseModel, field_validator
from typing import List
from services.commons.model import Meta



class CategoryModel(BaseModel):
    name: str
    uuid: str


    @field_validator("name", "uuid")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field must not be empty")
        else:
            return value


class CategoriesModel(BaseModel):
    categories: List[CategoryModel]
    meta: Meta

