import allure
from playwright.sync_api import APIRequestContext, APIResponse

from framework.clients.rest.base_client import BaseClient


class AuthClient(BaseClient):
    def __init__(self, api_context: APIRequestContext):
        super().__init__(api_context=api_context, api_path="auth", endpoint="login")

    @allure.step("POST request to the endpoint: /aut/login")
    def user_login(self, username: str, password: str) -> APIResponse:
        """
        Authenticates a user by sending his credentials to the `login` endpoint.

        Returns
        -------
        APIResponse
            An object containing the response details from the authentication request.
        """
        return self.api_context.post(
            url=self.url,
            form={
                "username": username,
                "password": password,
            },
        )
