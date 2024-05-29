from pydantic import BaseModel, field_validator, Field
from typing import List
from services.commons.model import Meta



class ItemModel(BaseModel):
    item_uuid: str = Field(..., min_length=36, max_length=36,
                           pattern=r'[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-['
                                   r'a-fA-F0-9]{12}')
    quantity: int = Field(..., ge=1, le=100)
    total_price: int = Field(..., ge=0)


    @field_validator("item_uuid", "quantity", "total_price")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field must not be empty")
        else:
            return value


class CartModel(BaseModel):
    items: List[ItemModel] = Field(..., max_items=10)
    total_price: int = Field(..., ge=0)
    user_uuid: str = Field(..., min_length=36, max_length=36,
                           pattern=r'[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-['
                                   r'a-fA-F0-9]{12}')

    @field_validator("items", "user_uuid")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field must not be empty")
        else:
            return value