import os

from dotenv import load_dotenv
from playwright.sync_api import APIResponse

load_dotenv()


def test_user_login2(auth_api_client):
    user_login = os.getenv("ADMIN_EMAIL")
    user_password = os.getenv("ADMIN_PASSWORD")

    response: APIResponse = auth_api_client.user_login(user_login, user_password)

    assert response.status == 200, f"Expected status code 200, but got {response.status}"
