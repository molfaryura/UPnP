"""Tests for basic IGD functionality."""

import miniupnpc

import utils


def test_valid_ip_address(config_upnp, log, igd: miniupnpc.UPnP, local_ip_address: str):
    """Test that a valid IP address is returned correctly."""

    external_ip_address = igd.externalipaddress()

    log.info("IGD IPv4 address: " + external_ip_address)
    log.info("Local IPv4 address: " + local_ip_address)

    assert utils.is_ip_address_valid(
        external_ip_address
    ), "IGD External IPv4 address is not valid"

    assert (
        external_ip_address != local_ip_address
    ), "External IP address is local IP address"


def test_device_info(config_upnp, log, igd: miniupnpc.UPnP, local_ip_address: str):
    """Test that device info is returned correctly."""

    lan_addr = igd.lanaddr
    log.info("Local IPv4 address: " + lan_addr)

    assert lan_addr and lan_addr == local_ip_address, "IGD LAN address is not valid"

    status_info = igd.statusinfo()
    log.info(f"Status: {status_info}")

    assert status_info, "IGD status info is not valid"
