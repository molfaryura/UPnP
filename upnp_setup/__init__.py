"""UPnP Setup Module"""

import os

from dotenv import load_dotenv

from .upnp import UpnpManager

load_dotenv()

ROUTER_PWD = os.getenv("ROUTER_PASSWORD")
LOGIN_URL = os.getenv("ROUTER_URL")

upnp_manager = UpnpManager(ROUTER_PWD, LOGIN_URL)
