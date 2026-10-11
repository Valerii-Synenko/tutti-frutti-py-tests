from framework.api.rest.models.user.user_request import LoginUserRequestModel
from framework.api.rest.models.user.user_response import LoginUserResponseModel, RegisterUserResponseModel
from qase.pytest import qase


class TestUser:
    """
    Test for user authentication functionality.

    Covers endpoints:
    -------
    `register`, `login`, `logout`, `refresh`, `get user`, `update user`, `become a seller`
    """

    @qase.id(55)
    def test_create_account(self, api_hub, user_for_registration):
        with qase.step("Register a new user via the API"):
            register_response = api_hub.auth_client.user_registration(user_for_registration)

            with qase.step("Assert response"):
                assert register_response.status == 201, f"Unexpected status code: {register_response.status}"
                user = RegisterUserResponseModel.model_validate(register_response.json())
                assert user.email == user_for_registration.email, "Unexpected user's email in the response."
                assert user.full_name == user_for_registration.full_name, "Unexpected user name in the response."
                assert not user.is_admin, "User was registered as an admin."
                assert not user.is_seller, "User was registered as a seller."

        with qase.step("Login via the API with the same user"):
            login_payload = LoginUserRequestModel(
                username=user_for_registration.email,
                password=user_for_registration.password,
            )
            login_response = api_hub.auth_client.user_login(login_payload)

            with qase.step("Assert response"):
                assert login_response.status == 200, f"Unexpected status code: {login_response.status}"
                LoginUserResponseModel.model_validate(login_response.json())
