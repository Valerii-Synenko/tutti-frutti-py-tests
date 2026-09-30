from __future__ import annotations

from faker import Faker
from polyfactory.factories.pydantic_factory import ModelFactory
from pydantic import BaseModel

faker = Faker()


class RegisterUserRequestModel(BaseModel):
    email: str
    password: str
    full_name: str


class RegisterUserRequestFactory(ModelFactory[RegisterUserRequestModel]):
    __model__ = RegisterUserRequestModel


class LoginUserRequestModel(BaseModel):
    username: str
    password: str


class LoginUserRequestFactory(ModelFactory[LoginUserRequestModel]):
    __model__ = LoginUserRequestModel
