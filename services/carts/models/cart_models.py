from pydantic import BaseModel, field_validator
from typing import List
from services.commons.model import Meta



class ItemModel(BaseModel):
    item_uuid: str
    quantity: int
    total_price: int


    @field_validator("item_uuid", "quantity", "total_price")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field must not be empty")
        else:
            return value


class CartModel(BaseModel):
    items: List[ItemModel]
    total_price: int
    user_uuid: str

    @field_validator("items", "user_uuid")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field must not be empty")
        else:
            return value