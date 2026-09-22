from playwright.sync_api import Page

from framework.ui.components.nav_bar import NavBar
from framework.ui.pages.base_page import BasePage


class MarketPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, "")
        self.nav_bar = NavBar(page)
