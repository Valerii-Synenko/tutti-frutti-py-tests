from playwright.sync_api import Page


class NavBar:
    """
    Navigation bar component.
    Depends on the page and user state, the navigation bar can contain different links.
    """

    def __init__(self, page: Page):
        self._nav_bar_component = page.get_by_test_id("navbar")
        self.market_link = self._nav_bar_component.get_by_label("Market")
        self.my_orders_link = self._nav_bar_component.get_by_label("My Orders")
        self.cart_link = self._nav_bar_component.get_by_label("Cart")
        self.user_link = self._nav_bar_component.get_by_test_id("nav-cabinet-link")
        self.login_button = self._nav_bar_component.get_by_test_id("nav-login-link")
