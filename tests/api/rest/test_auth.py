import os

from dotenv import load_dotenv
from playwright.sync_api import APIResponse

load_dotenv()


class AuthTest:
    """
    Test for user authentication functionality.

    Covers endpoints:
    -------
    `register`, `login`, `me`, `refresh`
    """

    def test_user_login(self, auth_api_client):
        user_login = os.getenv("ADMIN_EMAIL")
        user_password = os.getenv("ADMIN_PASSWORD")

        response: APIResponse = auth_api_client.user_login(user_login, user_password)

        assert response.status == 200, f"Expected status code 200, but got {response.status}"
