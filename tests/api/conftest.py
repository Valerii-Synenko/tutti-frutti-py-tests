from collections.abc import Generator

import pytest
from playwright.sync_api import APIRequestContext, Playwright


@pytest.fixture
def api_context(playwright: Playwright) -> Generator[APIRequestContext]:
    request_context = playwright.request.new_context()
    yield request_context
    request_context.dispose()
