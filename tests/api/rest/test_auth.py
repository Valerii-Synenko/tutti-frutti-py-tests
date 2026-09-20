import allure
import pytest
from constants import SUB_SUITE_LOGIN, SUITE_AUTH
from playwright.sync_api import APIResponse
from settings import settings


@allure.suite(SUITE_AUTH)
@allure.sub_suite(SUB_SUITE_LOGIN)
@pytest.mark.api
class TestAuth:
    """
    Test for user authentication functionality.

    Covers endpoints:
    -------
    `register`, `login`, `me`, `refresh`
    """

    @allure.id("TC-0001")
    @allure.title("Login as an admin")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_login(self, auth_api_client):
        with allure.step("Login as a user with admin's credentials."):
            user_login = settings.admin_email
            user_password = settings.admin_password
            response: APIResponse = auth_api_client.user_login(user_login, user_password)

        with allure.step("Check that status code is 200."):
            assert response.status == 200, f"Expected status code 200, but got {response.status}"
