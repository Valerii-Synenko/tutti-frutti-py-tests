from __future__ import annotations

from typing import Annotated, Literal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field

JWT = Annotated[str, Field(pattern=r"^[\w-]+\.[\w-]+\.[\w-]+$")]


class RegisterUserModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: UUID
    email: EmailStr
    full_name: str
    is_admin: bool
    is_seller: bool


class LoginUserModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

    access_token: JWT
    refresh_token: JWT
    token_type: Literal["Bearer", "bearer"]
