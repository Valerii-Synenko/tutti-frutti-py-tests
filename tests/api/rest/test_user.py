import allure
import pytest
from constants import SUB_SUITE_LOGIN, SUITE_AUTH
from framework.models.api.rest.user.login_response_model import LoginResponseModel
from framework.utils.assertions import assert_matches_schema
from playwright.sync_api import APIResponse
from settings import settings


@allure.suite(SUITE_AUTH)
@allure.sub_suite(SUB_SUITE_LOGIN)
@pytest.mark.api
class TestUser:
    """
    Test for user authentication functionality.

    Covers endpoints:
    -------
    `register`, `login`, `logout`, `refresh`, `get user`, `update user`, `become a seller`
    """

    @allure.id("TC-0001")
    @allure.title("Login as an admin")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("An admin have to have opportunity to login via common endpoint")
    def test_user_login(self, auth_api_client):
        with allure.step("Login as a user with admin's credentials."):
            response: APIResponse = auth_api_client.user_login(
                settings.admin_email, settings.admin_password
            )

        with allure.step("Validate response."):
            assert response.status == 200, f"Expected status code 200, but got {response.status}"
            assert_matches_schema(LoginResponseModel, response.json())
