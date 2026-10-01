from __future__ import annotations

from pydantic import BaseModel


class Attributes(BaseModel):
    shelf_life_days: int
    storage: str


class CreateFruitResponseModel(BaseModel):
    name: str
    slug: str
    description: str
    origin: str
    is_organic: bool
    seasonal_months: list[int]
    tags: list[str]
    image_url: str
    base_price_hint_eur: float
    initial_quantity: int
    attributes: Attributes
