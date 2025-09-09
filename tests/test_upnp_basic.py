""" """

import miniupnpc

import utils


def test_valid_ip_address(igd: miniupnpc.UPnP, local_ip_address: str):
    """Test that a valid IP address is returned correctly."""

    external_ip_address = igd.externalipaddress()

    assert (
        utils.is_ip_address_valid(external_ip_address)
        and external_ip_address != local_ip_address
    )
