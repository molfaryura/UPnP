""" """

import miniupnpc

import utils


def test_valid_ip_address(log, igd: miniupnpc.UPnP, local_ip_address: str):
    """Test that a valid IP address is returned correctly."""

    external_ip_address = igd.externalipaddress()

    log.info("IGD IPv4 address: " + external_ip_address)
    log.info("Local IPv4 address: " + local_ip_address)

    assert (
        utils.is_ip_address_valid(external_ip_address)
        and external_ip_address != local_ip_address
    )
