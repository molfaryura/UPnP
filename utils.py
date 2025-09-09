"""Helper functions for testing."""

import re


def is_ip_address_valid(ip_address):
    """Check if IP address is valid."""

    ipv4_pattern = (
        r"^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
        r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
        r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
        r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    )

    return re.match(ipv4_pattern, ip_address) is not None
