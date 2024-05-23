from pydantic import BaseModel, field_validator
from typing import List
from datetime import datetime
from services.carts.models.cart_models import ItemModel
from services.commons.model import Meta


class PaymentModel(BaseModel):
    order_uuid: str
    payment_method: str
    amount: int
    created_at: datetime
    status: str
    updated_at: datetime
    user_uuid: str
    uuid: str

    @field_validator("order_uuid", "user_uuid", "created_at", "status", "amount", "update_at", "uuid", "payment_method")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field must not be empty")
        else:
            return value


class PaymentsModel(BaseModel):
    mete: Meta
    payments: List[PaymentModel]

    @field_validator("payments", "meta")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field must not be empty")
        else:
            return value