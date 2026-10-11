from __future__ import annotations

from pydantic import BaseModel, ConfigDict, EmailStr


class RegisterUserRequestModel(BaseModel):
    model_config = ConfigDict(extra="allow")

    email: EmailStr
    password: str
    full_name: str


class LoginUserRequestModel(BaseModel):
    model_config = ConfigDict(extra="allow")

    username: EmailStr
    password: str
