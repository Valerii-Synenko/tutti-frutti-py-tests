import allure
import pytest
from constants import SUB_SUITE_LOGIN_UI, SUIT_LOGIN_PAGE
from framework.ui.pages.market_page import MarketPage
from playwright.sync_api import expect
from settings import settings


@allure.suite(SUIT_LOGIN_PAGE)
@allure.sub_suite(SUB_SUITE_LOGIN_UI)
@pytest.mark.ui
class TestAuth:
    """
    Tests related to the login logic.

    Covers cases:
    -------
    `login`, `registration`
    """

    @allure.id("TC-0002")
    @allure.title("Login as an admin via login form on the login page")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description(
        "An admin have to have opportunity to login via login form on the login page"
    )
    def test_admin_login(self, login_page):
        with allure.step("Login as admin"):
            market_page: MarketPage = login_page.goto().login(
                settings.admin_email, settings.admin_password
            )

        with allure.step("Check that the user's name is present on the Market page in the navbar"):
            expect(market_page.nav_bar.user_link).to_have_text(settings.admin_name)
