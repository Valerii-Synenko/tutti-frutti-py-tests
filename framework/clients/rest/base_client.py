import os

from playwright.sync_api import APIRequestContext


class BaseClient:
    def __init__(self, api_context: APIRequestContext, api_path: str, endpoint: str):
        self.api_context = api_context
        self.api_path = api_path
        self.endpoint = endpoint
        self.url = f"{os.getenv('BASE_API_URL')}/{self.api_path}/{self.endpoint}"
