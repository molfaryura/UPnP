"""Login page object model for Playwright tests."""

from playwright.sync_api import Page

from utils import logger


class LoginPage:
    """Login page object model"""

    def __init__(self, page: Page, url: str) -> None:
        """Initialize LoginPage with the given Playwright page and URL."""

        self.page = page
        self.url = url
        self.password_field = page.get_by_role(
            "textbox", name="Введіть пароль користувача"
        )
        self.button = page.get_by_role("button", name="Вхід")

    def enter_password(self, password: str) -> None:
        """Enter the password into the password field."""

        try:
            self.page.goto(self.url)
        except Exception as e:
            logger.error(f"Failed to navigate to {self.url}: {e}")
            raise

        try:
            self.password_field.fill(password)
        except Exception as e:
            logger.error(f"Failed to fill password field: {e}")
            raise

    def click_next(self) -> None:
        """Click the login button to proceed."""

        try:
            self.button.click(delay=100)
        except Exception as e:
            logger.error(f"Failed to click login button: {e}")
            raise
