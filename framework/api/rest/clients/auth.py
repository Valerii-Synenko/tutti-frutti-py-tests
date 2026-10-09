from playwright.sync_api import APIRequestContext, APIResponse
from qase.pytest import qase

from framework.api.rest.clients.base import BaseClient
from framework.api.rest.models.user.user_request import LoginUserRequestModel, RegisterUserRequestModel


class AuthClient(BaseClient):
    def __init__(self, api_context: APIRequestContext):
        super().__init__(api_context=api_context, api_path="auth")
        self.login_endpoint = "/login"
        self.register_endpoint = "/register"

    @qase.step("POST request to the endpoint: /auth/login")
    def user_login(self, payload: LoginUserRequestModel) -> APIResponse:
        """
        Authenticates a user by sending his credentials to the `login` endpoint.

        Returns
        -------
        APIResponse
            An object containing the response details from the authentication request.
        """
        return self.api_context.post(
            url=self.base_url + self.login_endpoint,
            form=payload.model_dump(),
        )

    @qase.step("POST request to the endpoint: /auth/register")
    def user_registration(self, payload: RegisterUserRequestModel) -> APIResponse:
        """
        Registers a new user by sending his credentials to the `registration` endpoint.

        Returns
        -------
        APIResponse
            An object containing the response details from the registration request.
        """
        return self.api_context.post(
            url=self.base_url + self.register_endpoint,
            data=payload.model_dump(),
        )
