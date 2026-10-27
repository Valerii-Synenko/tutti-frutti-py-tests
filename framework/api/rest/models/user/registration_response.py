from typing import Any
from uuid import UUID

from openai import BaseModel
from pydantic import ConfigDict, EmailStr


# Registration
class RegisterUserModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: UUID
    email: EmailStr
    full_name: str
    is_admin: bool
    is_seller: bool


# Invalid registration
class MinLengthCtx(BaseModel):
    model_config = ConfigDict(extra="forbid")
    min_length: int


class EmailCtx(BaseModel):
    model_config = ConfigDict(extra="forbid")
    reason: str


class DetailItem(BaseModel):
    type: str
    loc: list[str | int]
    msg: str
    input: Any
    ctx: MinLengthCtx | EmailCtx | None = None


class InvalidRegistrationModel(BaseModel):
    detail: list[DetailItem]
