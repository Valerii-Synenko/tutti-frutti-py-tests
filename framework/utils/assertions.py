import allure
import pytest
from pydantic import BaseModel, ValidationError


@allure.step("assert pydantic model matching schema")
def assert_matches_schema[T: BaseModel](model: type[T], data: dict) -> T:
    """
    Asserts that the given data matches the schema of the provided Pydantic model.

    Parameters
    -------
    model : T: BaseModel
        An instance of a Pydantic BaseModel class.
    data : dict
        A dictionary containing the data to be validated against the model's schema.

    Returns
    -------
    An instance of the provided Pydantic model class.

    """
    data_marker = "Response" if "Response" in model.__name__ else "Data"

    try:
        return model.model_validate(data)
    except ValidationError as e:
        pytest.fail(f"{data_marker} does not match {model.__name__} schema:\n{e}")
