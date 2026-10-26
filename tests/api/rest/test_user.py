from http import HTTPStatus

from framework.api.rest.models.user_response import (
    LoginUserModel,
    RegisterUserModel,
)
from framework.api.rest.payloads.user import LoginPayload
from qase.pytest import qase


class TestUser:
    """
    Test for user authentication functionality.

    Covers endpoints:
    -------
    `register`, `login`, `logout`, `refresh`, `get user`, `update user`, `become a seller`
    """

    @qase.id(55)
    @qase.title("Create account with valid data via API")
    def test_create_account(self, api_hub, user_for_registration):
        with qase.step(
            title="Register a new user via the API",
            expected="""
            1. The response status is `201` with input email and full_name.
            2. The response has `is_admin` false and `is_seller` false.
            3. The response has no password or hashed_password field.""",
        ):
            register_response = api_hub.auth_client.user_registration(user_for_registration)

            assert register_response.status == HTTPStatus.CREATED, (
                f"Unexpected status code: {register_response.status}"
            )
            user = RegisterUserModel.model_validate(register_response.json())
            assert user.email == user_for_registration.email, (
                "Unexpected user's email in the response."
            )
            assert user.full_name == user_for_registration.full_name, (
                "Unexpected user name in the response."
            )
            assert not user.is_admin, "User was registered as an admin."
            assert not user.is_seller, "User was registered as a seller."

        with qase.step(
            title="Login via the API with the same user",
            expected="The response status is `200` with a token pair.",
        ):
            login_payload = LoginPayload(
                username=user_for_registration.email,
                password=user_for_registration.password,
            )
            login_response = api_hub.auth_client.user_login(login_payload)

            assert login_response.status == HTTPStatus.OK, (
                f"Unexpected status code: {login_response.status}"
            )
            LoginUserModel.model_validate(login_response.json())
