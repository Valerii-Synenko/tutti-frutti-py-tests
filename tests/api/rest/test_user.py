import allure
import pytest
from constants import REST_API_SUB_SUITE_LOGIN, REST_API_SUITE_AUTH
from framework.models.api.rest.user.login_response import LoginResponseModel
from framework.utils.assertions import assert_matches_schema
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
    @allure.title("Login as an admin")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("An admin have to have opportunity to login via common endpoint")
    def test_user_login(self, auth_api_client, admin_user):
        with allure.step("Login as a user with admin's credentials."):
            response: APIResponse = auth_api_client.user_login(
                admin_user.email, admin_user.password
            )

        with allure.step("Validate response."):
            assert response.status == 200, f"Expected status code 200, but got {response.status}"
            assert_matches_schema(LoginResponseModel, response.json())
