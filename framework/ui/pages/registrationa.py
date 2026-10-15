from playwright.sync_api import Page
from qase.pytest import qase

from framework.ui.pages.base_page import BasePage
from framework.ui.pages.login_page import LoginPage


class RegistrationPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page, "/register")
        self.auth_form = self.page.locator(".auth-card")
        self.login_link = self.auth_form.get_by_text("Log in")

    @qase.step("Click on `Log in` link on the auth-form")
    def click_login_link(self) -> LoginPage:
        self.login_link.click()
        return LoginPage(self.page)
