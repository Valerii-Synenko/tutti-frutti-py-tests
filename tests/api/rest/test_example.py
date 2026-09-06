import os

import requests
from dotenv import load_dotenv
from requests import Response

load_dotenv()


def test_admin_login():
    resp: Response = requests.post(
        url="http://localhost:8080/auth/login",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={
            "username": f"{os.getenv('ADMIN_EMAIL')}",
            "password": f"{os.getenv('ADMIN_PASSWORD')}",
        },
    )
    assert resp.status_code == 200
