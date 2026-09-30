from playwright.sync_api import APIRequestContext
from settings import settings


class BaseClient:
    def __init__(
        self,
        api_context: APIRequestContext,
        api_path: str,
    ):
        self.api_context = api_context
        self.api_path = api_path
        self.base_url = f"{settings.base_api_url}/{self.api_path}"
