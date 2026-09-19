from playwright.sync_api import APIResponse
from settings import settings


class TestAuth:
    """
    Test for user authentication functionality.

    Covers endpoints:
    -------
    `register`, `login`, `me`, `refresh`
    """

    def test_user_login(self, auth_api_client):
        user_login = settings.admin_email
        user_password = settings.admin_password

        response: APIResponse = auth_api_client.user_login(user_login, user_password)

        assert response.status == 200, f"Expected status code 200, but got {response.status}"
