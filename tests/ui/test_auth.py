from framework.ui.pages.login_page import LoginPage
from framework.ui.pages.market_page import MarketPage
from playwright.sync_api import expect
from qase.pytest import qase


class TestAuth:
    """
    Tests related to the login and registration logic.

    Covers cases:
    -------
    `login`, `registration`
    """

    @qase.id(56)
    @qase.title("Happy path: User logs in.")
    def test_successful_login(self, login_page, regular_user):
        with qase.step(
            title="Login as a user",
            expected="1. The user is redirected to the Market page.\n"
            "2. The NavBar shows the user's full name.\n"
            "3. The `Logout button` is visible.\n"
            "4. The `Login button` is not visible.",
        ):
            market_page: MarketPage = login_page.goto().login(
                email=regular_user.email,
                password=regular_user.password,
            )

            expect(
                market_page.page,
                "The Market page did not open.",
            ).to_have_url(market_page.page_url)

            expect(
                market_page.nav_bar.user_link,
                "Missing user name in the NavBar.",
            ).to_have_text(regular_user.full_name)

            expect(
                market_page.nav_bar.logout_button,
                "Logout button is missing from the NavBar",
            ).to_be_visible()

            expect(
                market_page.nav_bar.login_button,
                "Login button is present in the NavBar.",
            ).not_to_be_visible()

    @qase.id(41)
    @qase.title("Open Login page from registration form")
    def test_open_login_page_from_registration_form(self, registration_page):
        with qase.step(
            title="Click the `Log in` link under the form", expected="The Login page is opened."
        ):
            login_page: LoginPage = registration_page.goto().click_login_link()

            expect(login_page.page, "The `Login page` did not open.").to_have_url(
                login_page.page_url
            )

            expect(login_page.login_button, "There is not visible `Login button`.").to_be_visible()

    @qase.id(38)
    @qase.title("Checks that a logged-in user stays logged in after reloading the page.")
    def test_user_logged_in_after_page_reload(self, market_page, regular_user):
        with qase.step(
            title="Reload current page",
            expected="""
            1. The NavBar still shows the user's full name.
            2. The `Log out` button is visible.
            """,
        ):
            market_page = market_page.goto(bearer=regular_user.bearer_token)
            market_page.page.reload()

            expect(market_page.nav_bar.logout_button, "Missing `Log out` button").to_be_visible()
            expect(market_page.nav_bar.user_link, "Mussing user name from navbar").to_have_text(
                regular_user.full_name
            )
