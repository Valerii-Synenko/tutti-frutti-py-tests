from __future__ import annotations

from typing import Annotated

from constants import LATIN_LETTERS_STRICT
from polyfactory.factories.pydantic_factory import ModelFactory
from pydantic import BaseModel, EmailStr, Field


class RegisterUserRequestModel(BaseModel):
    email: EmailStr
    password: str
    full_name: Annotated[str, Field(min_length=1, pattern=LATIN_LETTERS_STRICT)]


class RegisterUserRequestFactory(ModelFactory[RegisterUserRequestModel]):
    __model__ = RegisterUserRequestModel


class LoginUserRequestModel(BaseModel):
    username: EmailStr
    password: str


class LoginUserRequestFactory(ModelFactory[LoginUserRequestModel]):
    __model__ = LoginUserRequestModel
