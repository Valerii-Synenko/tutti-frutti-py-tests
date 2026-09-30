import allure
import pytest
from constants import REST_API_SUB_SUITE_LOGIN, REST_API_SUITE_AUTH
from framework.api.rest.models.user.user_response import RegisterUserResponseModel
from playwright.sync_api import APIResponse


@allure.suite(REST_API_SUITE_AUTH)
@allure.sub_suite(REST_API_SUB_SUITE_LOGIN)
@pytest.mark.api
class TestUser:
    """
    Test for user authentication functionality.

    Covers endpoints:
    -------
    `register`, `login`, `logout`, `refresh`, `get user`, `update user`, `become a seller`
    """

    @allure.id("TC-0001")
    @allure.title("New user registration")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Testa verify that new user can be registered")
    def test_user_registration(self, api_hub, user_for_registration):
        with allure.step("Register a new user."):
            response: APIResponse = api_hub.auth_client.user_registration(user_for_registration)

        with allure.step("Validate response."):
            assert response.status == 201, f"Expected status code 201, but got {response.status}"
            RegisterUserResponseModel.model_validate(response.json())
