"""Module to manage UPnP settings on a router via web interface automation."""

import os

from playwright.sync_api import sync_playwright, ElementHandle

from dotenv import load_dotenv

from utils import logger

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

        try:
            return self.__config_upnp(True)
        except Exception as e:
            logger.error(f"Failed to turn on UPnP: {e}")
            raise

    def turn_off_upnp(self) -> ElementHandle | None:
        """Turn off UPnP setting on the router."""

        try:
            return self.__config_upnp(False)
        except Exception as e:
            logger.error(f"Failed to turn off UPnP: {e}")
            raise

    def __config_upnp(self, state) -> ElementHandle | None:
        """Helper method to configure UPnP setting on the router to the desired state."""

        with sync_playwright() as p:
            logger.info(f"Configuring UPnP settings. Desired state: {state}")
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            login_page = LoginPage(page=page, url=self.login_url)
            logger.info("Navigating to login page...")
            logger.info("Login page opened. Entering password...")
            login_page.enter_password(self.password)
            logger.info("Clicking login button...")
            login_page.click_next()

            settings_page = SettingsPage(page=page)
            logger.info("Clicking settings page...")
            settings_page.click_settings()
            logger.info("Clicking web menu...")
            settings_page.click_web()

            upnp_page = UpnpPage(page=page)
            logger.info("Clicking UPnP page...")
            upnp_page.go_to_upnp()
            logger.info("Waiting for page to load completely...")
            page.wait_for_function("document.readyState === 'complete'")
            logger.info(f"Changing UPnP state to {state}...")
            changed = upnp_page.change_upnp_state(state)

            logger.info("Configuring is done. Closing browser...")
            browser.close()

        return changed
