import pytest
from framework.ui.pages.login_page import LoginPage
from framework.ui.pages.market_page import MarketPage
from playwright.sync_api import Page
from qase.pytest import qase


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """Attaches a screenshot of the page to the Qase result when a UI test fails."""
    outcome = yield
    report = outcome.get_result()

    page = item.funcargs.get("page")
    if report.failed and page and not page.is_closed():
        qase.attach((page.screenshot(full_page=True), "image/png", f"{report.when}-failure.png"))


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def market_page(page: Page) -> MarketPage:
    return MarketPage(page)
