from dataclasses import asdict

from playwright.sync_api import APIRequestContext, APIResponse
from qase.pytest import qase

from framework.api.rest.clients.base import BaseClient
from framework.api.rest.payloads.user import LoginPayload, RegisterPayload


class AuthClient(BaseClient):
    def __init__(self, api_context: APIRequestContext):
        super().__init__(api_context=api_context, api_path="auth")
        self.login_endpoint = "/login"
        self.register_endpoint = "/register"

    @qase.step("POST request to the endpoint: /auth/login")
    def user_login(self, payload: LoginPayload) -> APIResponse:
        """
        Authenticates a user by sending his credentials to the `login` endpoint.

        Returns
        -------
        APIResponse
            An object containing the response details from the authentication request.
        """
        return self.api_context.post(
            url=self.base_url + self.login_endpoint,
            form=asdict(payload),
        )

    @qase.step("POST request to the endpoint: /auth/register")
    def user_registration(self, payload: RegisterPayload) -> APIResponse:
        """
        Registers a new user by sending his credentials to the `registration` endpoint.

        Returns
        -------
        APIResponse
            An object containing the response details from the registration request.
        """
        return self.api_context.post(
            url=self.base_url + self.register_endpoint,
            data=asdict(payload),
        )
