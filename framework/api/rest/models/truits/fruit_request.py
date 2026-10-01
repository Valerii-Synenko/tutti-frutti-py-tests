from typing import Annotated

from constants import LATIN_LETTERS
from polyfactory.factories.pydantic_factory import ModelFactory
from pydantic import BaseModel, Field

Month = Annotated[int, Field(ge=1, le=12)]
Tag = Annotated[str, Field(min_length=1, max_length=10, pattern=LATIN_LETTERS)]


class FruitAttributes(BaseModel):
    shelf_life_days: Annotated[int, Field(gt=0, lt=50)]
    storage: Annotated[str, Field(min_length=1, max_length=10, pattern=LATIN_LETTERS)]


class FruitAttributesFactory(ModelFactory[FruitAttributes]):
    __model__ = FruitAttributes


class CreateFruitRequestModel(BaseModel):
    name: Annotated[str, Field(min_length=1, max_length=120, pattern=LATIN_LETTERS)]
    slug: Annotated[str, Field(min_length=1, max_length=120, pattern=LATIN_LETTERS)]
    description: Annotated[str, Field(min_length=1, max_length=2000)]
    origin: Annotated[str, Field(min_length=4, max_length=45, pattern=LATIN_LETTERS)]
    is_organic: bool
    seasonal_months: Annotated[set[Month], Field(min_length=1, max_length=5)]
    tags: Annotated[set[Tag], Field(min_length=10, max_length=20, pattern=LATIN_LETTERS)]
    image_url: Annotated[str, Field(min_length=1, max_length=100)]
    base_price_hint_eur: Annotated[float, Field(gt=0.0)]
    initial_quantity: Annotated[int, Field(gt=0)]
    attributes: FruitAttributes


class CreateFruitRequestFactory(ModelFactory[CreateFruitRequestModel]):
    __model__ = CreateFruitRequestModel
