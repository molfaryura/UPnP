"""Settings page object model for Playwright tests."""

from playwright.sync_api import Page

from utils import logger


class SettingsPage:
    """Settings page object model"""

    def __init__(self, page: Page) -> None:
        """Initialize SettingsPage with the given Playwright page."""

        self.page = page
        self.settings = page.get_by_role("menuitem", name="Додатково")
        self.web = page.get_by_role("menuitem", name="Мережа")

    def click_settings(self):
        """Click on the Settings menu item."""

        try:
            self.settings.click(delay=100)
        except Exception as e:
            logger.error(f"Failed to click settings menu item: {e}")
            raise

    def click_web(self):
        """Click on the Web menu item."""

        try:
            self.web.click(delay=100)
        except Exception as e:
            logger.error(f"Failed to click web menu item: {e}")
            raise
