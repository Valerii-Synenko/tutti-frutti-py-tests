import pytest
from framework.ui.pages.login_page import LoginPage
from framework.ui.pages.market_page import MarketPage
from playwright.sync_api import Page


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def market_page(page: Page) -> MarketPage:
    return MarketPage(page)
