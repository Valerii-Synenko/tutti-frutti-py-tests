from functools import cached_property

from playwright.sync_api import APIRequestContext

from framework.api.clients.rest import AuthClient


class ApiHub:
    def __init__(self, api_context: APIRequestContext):
        self._api_context = api_context

    @cached_property
    def auth_client(self) -> AuthClient:
        return AuthClient(self._api_context)
