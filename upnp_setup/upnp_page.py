"""UPnP page object model"""

from playwright.sync_api import Page, ElementHandle


class UpnpPage:
    """UPnP page object model"""

    def __init__(self, page: Page) -> None:
        """Initialize UpnpPage with the given Playwright page."""

        self.page = page
        self.upnp_menu = page.get_by_role("menuitem", name="UPnP")
        self.switch = page.get_by_role("switch")
        self.success_selector = "div:has-text('Конфігурація успішна')"

    def go_to_upnp(self) -> None:
        """Navigate to the UPnP settings page."""

        self.upnp_menu.click()

    def change_upnp_state(self, state: bool) -> ElementHandle | None:
        """Change the UPnP state to the desired state."""

        if self.__check_upnp_state(state):
            self.switch.click()
            return self.page.wait_for_selector(self.success_selector)
        return None

    def __check_upnp_state(self, state) -> bool:
        """Helper method to check the current UPnP state."""

        if state:
            return not self.switch.is_checked()
        else:
            return self.switch.is_checked()
