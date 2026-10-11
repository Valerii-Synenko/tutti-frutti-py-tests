from framework.ui.pages.market_page import MarketPage
from playwright.sync_api import expect
from qase.pytest import qase
from settings import settings


class TestAuth:
    """
    Tests related to the login and registration logic.

    Covers cases:
    -------
    `login`, `registration`
    """

    @qase.id(37)
    def test_successful_login(self, login_page, buyer_user):
        with qase.step("Login as the buyer"):
            market_page: MarketPage = login_page.goto().login(
                email=buyer_user.email,
                password=buyer_user.password,
            )
            with qase.step("Assert expected result"):
                expect(
                    market_page.page,
                    "User must be redirected to the Market page after success logging.",
                ).to_have_url(settings.market_page_url)

                expect(
                    market_page.nav_bar.user_link,
                    "Missing user name in the NavBar but it must be present there.",
                ).to_have_text(buyer_user.full_name)

                expect(
                    market_page.nav_bar.logout_button,
                    "Logout button is missing from the NavBar but it must be visible for the logged user",
                ).to_be_visible()

                expect(
                    market_page.nav_bar.login_button,
                    "The Login button must not be visible in the NavBar for the logged user",
                ).not_to_be_visible()
