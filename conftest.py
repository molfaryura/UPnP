"""Pytest configuration."""

import socket

import logging

import pytest

import miniupnpc

from upnp_setup import upnp_manager

from utils import setup_logger


@pytest.fixture(scope="session")
def log():
    """Fixture to set up logging for tests."""

    return setup_logger(name="test_logger", log_file="logs/test_log.log")


@pytest.fixture(scope="session")
def config_upnp(log: logging.Logger):
    """Fixture to configure UPnP before and after tests."""

    (
        log.info("UPnP enabled")
        if upnp_manager.turn_on_upnp() is not None
        else log.info("UPnP is already enabled")
    )

    yield upnp_manager

    (
        log.info("UPnP disabled")
        if upnp_manager.turn_off_upnp() is not None
        else log.info("UPnP is already disabled")
    )


@pytest.fixture(scope="session")
def igd() -> miniupnpc.UPnP:
    """Fixture to get IGD instance"""
    upnp = miniupnpc.UPnP()
    upnp.discoverdelay = 2000

    try:
        upnp.discover()
        upnp.selectigd()
    except Exception as e:
        pytest.skip(f"UPnP discovery and selection failed: {e}")

    return upnp


@pytest.fixture(scope="session")
def local_ip_address() -> str:
    """Fixture to get local IP address."""

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
