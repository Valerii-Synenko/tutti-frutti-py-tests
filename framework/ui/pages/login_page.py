import allure
from playwright.sync_api import Page

from framework.ui.components.nav_bar import NavBar
from framework.ui.pages.base_page import BasePage
from framework.ui.pages.market_page import MarketPage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, "/login")
        self.nav_bar = NavBar(page)
        self.email_input = self.page.get_by_label("Email")
        self.password_input = self.page.get_by_label("Password")
        self.login_button = self.page.get_by_role("button", name="Log in")

    @allure.step("Login as a user")
    def login(self, email: str, password: str) -> MarketPage:
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()
        return MarketPage(self.page)
