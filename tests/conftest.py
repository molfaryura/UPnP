"""Pytest configuration."""

import socket

import pytest

import miniupnpc


@pytest.fixture(scope="session")
def igd() -> miniupnpc.UPnP:
    """Fixture to get IGD instance"""

    upnp = miniupnpc.UPnP()
    upnp.discoverdelay = 800

    if upnp.discover() <= 0:
        pytest.skip("Can not find UPnP IGD.")

    upnp.selectigd()

    return upnp


@pytest.fixture(scope="session")
def local_ip_address() -> str:
    """Fixture to get local IP address."""

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
