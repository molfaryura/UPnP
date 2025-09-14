"""Login page object model for Playwright tests."""

from playwright.sync_api import Page


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

        self.page.goto(self.url)
        self.password_field.fill(password)

    def click_next(self) -> None:
        """Click the login button to proceed."""

        self.button.click(delay=100)
