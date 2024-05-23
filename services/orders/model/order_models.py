from pydantic import BaseModel, field_validator
from typing import List
from datetime import datetime
from services.carts.models.cart_models import ItemModel
from services.commons.model import Meta


class OrderModel(BaseModel):
    created_at: datetime
    items: List[ItemModel]
    status: str
    total_price: int
    updated_at: datetime
    user_uuid: str
    uuid: str

    @field_validator("items", "user_uuid", "created_at", "status", "total_price", "update_at", "uuid")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field must not be empty")
        else:
            return value


class OrdersModel(BaseModel):
    mete: Meta
    orders: List[OrderModel]

    @field_validator("orders", "meta")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field must not be empty")
        else:
            return value