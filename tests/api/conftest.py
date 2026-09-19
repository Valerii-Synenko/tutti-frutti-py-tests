import pytest
from framework.clients.rest.auth_client import AuthClient


@pytest.fixture
def auth_api_client(api_context):
    return AuthClient(api_context)
