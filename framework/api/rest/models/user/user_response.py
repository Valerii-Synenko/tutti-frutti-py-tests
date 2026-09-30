from __future__ import annotations

from typing import Annotated, Literal
from uuid import UUID

from pydantic import BaseModel, Field

JWT = Annotated[str, Field(min_length=1, pattern=r"^[\w-]+\.[\w-]+\.[\w-]+$")]


class RegisterUserResponseModel(BaseModel):
    id: UUID
    email: str
    full_name: str
    is_admin: bool
    is_seller: bool


class LoginUserResponseModel(BaseModel):
    access_token: JWT
    refresh_token: JWT
    token_type: Literal["Bearer", "bearer"]
