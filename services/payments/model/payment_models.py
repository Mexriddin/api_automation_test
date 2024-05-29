from pydantic import BaseModel, field_validator, Field
from typing import List, Literal
from datetime import datetime
from services.commons.model import Meta


class PaymentModel(BaseModel):
    order_uuid: str = Field(..., min_length=36, max_length=36,
                            pattern=r'[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-['
                                    r'a-fA-F0-9]{12}')
    payment_method: Literal["card", "paypal", "wechat_pay", "mir_pay"]
    amount: int = Field(..., ge=0)
    created_at: datetime
    status: Literal["processing", "succeeded", "canceled"]
    updated_at: datetime
    user_uuid: str = Field(..., min_length=36, max_length=36,
                           pattern=r'[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-['
                                   r'a-fA-F0-9]{12}')
    uuid: str = Field(..., min_length=36, max_length=36,
                      pattern=r'[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-['
                              r'a-fA-F0-9]{12}')

    @field_validator("order_uuid", "user_uuid", "created_at", "status", "amount", "updated_at", "uuid",
                     "payment_method", check_fields=False)
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field must not be empty")
        else:
            return value


class PaymentsModel(BaseModel):
    mete: Meta
    payments: List[PaymentModel]

    @field_validator("payments", "meta", check_fields=False)
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field must not be empty")
        else:
            return value
