import pytest
from constants import QASE_SUITE_LOGIN
from framework.ui.pages.market_page import MarketPage
from playwright.sync_api import expect
from qase.pytest import qase


@pytest.mark.ui
class TestAuth:
    """
    Tests related to the login and registration logic.

    Covers cases:
    -------
    `login`, `registration`
    """

    @qase.id(37)
    @qase.suite(QASE_SUITE_LOGIN)
    @qase.title("Login as an admin via login form on the login page")
    @qase.severity("critical")
    @qase.description("An admin have to have opportunity to login via login form on the login page")
    def test_admin_login(self, login_page, admin_user):
        with qase.step("Login as admin"):
            market_page: MarketPage = login_page.goto().login(admin_user.email, admin_user.password)

        with qase.step("Check that the user's name is present on the Market page in the navbar"):
            expect(market_page.nav_bar.user_link).to_have_text(admin_user.full_name)
