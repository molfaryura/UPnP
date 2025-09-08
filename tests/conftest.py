"""Pytest configuration."""

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
