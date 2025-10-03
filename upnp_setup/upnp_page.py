"""UPnP page object model"""

from playwright.sync_api import Page, ElementHandle

from utils import logger


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

        try:
            self.upnp_menu.click()
        except Exception as e:
            logger.error(f"Failed to click UPnP menu item: {e}")
            raise

    def change_upnp_state(self, state: bool) -> ElementHandle | None:
        """Change the UPnP state to the desired state."""

        if self.__check_upnp_state(state):
            try:
                self.switch.click(delay=300)
                return self.page.wait_for_selector(self.success_selector)
            except Exception as e:
                logger.error(f"Failed to change UPnP state: {e}")
                raise
        return None

    def __check_upnp_state(self, state) -> bool:
        """Helper method to check the current UPnP state."""

        try:
            if state:
                return not self.switch.is_checked()
            else:
                return self.switch.is_checked()
        except Exception as e:
            logger.error(f"Failed to check UPnP state: {e}")
            raise
