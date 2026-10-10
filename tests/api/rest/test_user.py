from framework.api.rest.models.user.user_response import RegisterUserResponseModel
from playwright.sync_api import APIResponse
from qase.pytest import qase


class TestUser:
    """
    Test for user authentication functionality.

    Covers endpoints:
    -------
    `register`, `login`, `logout`, `refresh`, `get user`, `update user`, `become a seller`
    """

    @qase.id(55)
    def test_user_registration(self, api_hub, user_for_registration):
        with qase.step("Register a new user."):
            response: APIResponse = api_hub.auth_client.user_registration(user_for_registration)

        with qase.step("Validate response."):
            assert response.status == 201, f"Expected status code 201, but got {response.status}"
            RegisterUserResponseModel.model_validate(response.json())
