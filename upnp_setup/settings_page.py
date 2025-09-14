"""Settings page object model for Playwright tests."""

from playwright.sync_api import Page


class SettingsPage:
    """Settings page object model"""

    def __init__(self, page: Page) -> None:
        """Initialize SettingsPage with the given Playwright page."""

        self.page = page
        self.settings = page.get_by_role("menuitem", name="Додатково")
        self.web = page.get_by_role("menuitem", name="Мережа")

    def click_settings(self):
        """Click on the Settings menu item."""

        self.settings.click(delay=100)

    def click_web(self):
        """Click on the Web menu item."""

        self.web.click(delay=100)
