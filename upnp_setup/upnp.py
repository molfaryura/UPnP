"""Module to manage UPnP settings on a router via web interface automation."""

import os

from playwright.sync_api import sync_playwright, ElementHandle

from dotenv import load_dotenv

from .upnp_page import UpnpPage
from .login_page import LoginPage
from .settings_page import SettingsPage

load_dotenv()

ROUTER_PWD = os.getenv("ROUTER_PASSWORD")
LOGIN_URL = os.getenv("ROUTER_URL")


class UpnpManager:
    """Class to manage UPnP settings on a router via web interface automation."""

    def __init__(self, password, login_url) -> None:
        """Initialize UpnpManager with router credentials and URL."""

        self.password = password
        self.login_url = login_url

    def turn_on_upnp(self) -> ElementHandle | None:
        """Turn on UPnP setting on the router."""

        return self.__config_upnp(True)

    def turn_off_upnp(self) -> ElementHandle | None:
        """Turn off UPnP setting on the router."""

        return self.__config_upnp(False)

    def __config_upnp(self, state) -> ElementHandle | None:
        """Helper method to configure UPnP setting on the router to the desired state."""

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            login_page = LoginPage(page=page, url=self.login_url)
            login_page.enter_password(self.password)
            login_page.click_next()
            settings_page = SettingsPage(page=page)
            settings_page.click_settings()
            settings_page.click_web()
            upnp_page = UpnpPage(page=page)
            upnp_page.go_to_upnp()
            page.wait_for_function("document.readyState === 'complete'")
            changed = upnp_page.change_upnp_state(state)
            browser.close()

        return changed
