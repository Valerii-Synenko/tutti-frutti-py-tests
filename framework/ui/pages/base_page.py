from typing import Self

from playwright.sync_api import Page
from qase.pytest import qase
from settings import settings

from framework.ui.components.nav_bar import NavBar


class BasePage:
    def __init__(self, page: Page, page_path: str):
        self.page = page
        self.page_url = settings.base_ui_url + page_path
        self.nav_bar = NavBar(self.page)

    def __repr__(self) -> str:
        """
        Returns the name of the class to attach it to the report.
        It needs to be able to see the name of the called class in the report.
        """
        return self.__class__.__name__

    def goto(self) -> Self:
        with qase.step(f"Go to {self}"):
            self.page.goto(self.page_url)
        return self
