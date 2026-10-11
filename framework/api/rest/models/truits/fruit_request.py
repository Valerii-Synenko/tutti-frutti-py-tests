from decimal import Decimal
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

Month = Annotated[int, Field(ge=1, le=12)]
Tag = Annotated[str, Field(min_length=1, max_length=10)]


class FruitAttributes(BaseModel):
    model_config = ConfigDict(extra="allow")

    shelf_life_days: int
    storage: str


class CreateFruitRequestModel(BaseModel):
    model_config = ConfigDict(extra="allow")

    name: str
    slug: str
    description: str
    origin: str
    is_organic: bool
    seasonal_months: Annotated[set[Month], Field(min_length=1, max_length=5)]
    tags: Annotated[set[Tag], Field(min_length=10, max_length=20)]
    image_url: str
    base_price_hint_eur: Decimal
    initial_quantity: int
    attributes: FruitAttributes
