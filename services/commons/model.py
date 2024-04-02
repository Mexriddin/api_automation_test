from pydantic import BaseModel, field_validator


class Meta(BaseModel):
    total: int

    @field_validator("total")
    def field_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field must not be empty")
        else:
            return value


class ErrorModel(BaseModel):
    code: int
    message: str

    @field_validator("code", "message")
    def field_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field must not be empty")
        else:
            return value

