import os

from dotenv import load_dotenv
from playwright.sync_api import APIResponse

load_dotenv()


def test_admin_login(api_context):
    resp: APIResponse = api_context.post(
        "http://localhost:8080/auth/login",
        form={
            "username": f"{os.getenv('ADMIN_EMAIL')}",
            "password": f"{os.getenv('ADMIN_PASSWORD')}",
        },
    )

    assert resp.status == 200, f"Expected status code 200, but got {resp.status}"
