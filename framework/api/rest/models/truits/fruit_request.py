from typing import Annotated

from polyfactory.factories.pydantic_factory import ModelFactory
from pydantic import BaseModel, Field

Month = Annotated[int, Field(ge=1, le=12)]


class FruitAttributes(BaseModel):
    shelf_life_days: Annotated[int, Field(gt=0, lt=11)]
    storage: Annotated[str, Field(min_length=1, max_length=20)]


class FruitAttributesFactory(ModelFactory[FruitAttributes]):
    __model__ = FruitAttributes


class CreateFruitRequestModel(BaseModel):
    name: Annotated[str, Field(min_length=1, max_length=20)]
    slug: Annotated[str, Field(min_length=1, max_length=20)]
    description: Annotated[str, Field(min_length=1, max_length=20)]
    origin: Annotated[str, Field(min_length=1, max_length=20)]
    is_organic: bool
    seasonal_months: Annotated[list[Month], Field(min_length=1, max_length=12)]
    tags: Annotated[list[str], Field(min_length=1)]
    image_url: Annotated[str, Field(min_length=1, max_length=100)]
    base_price_hint_eur: Annotated[float, Field(gt=0.0)]
    attributes: FruitAttributes


class CreateFruitRequestFactory(ModelFactory[CreateFruitRequestModel]):
    __model__ = CreateFruitRequestModel


asd = CreateFruitRequestFactory.build(
    attributes=FruitAttributesFactory.build(
        factory_use_construct=True,
    ),
    factory_use_construct=True,
)

print(asd)
