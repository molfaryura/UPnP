"""Helper functions for testing."""

import re

import logging


def is_ip_address_valid(ip_address) -> bool:
    """Check if IP address is valid."""

    ipv4_pattern = (
        r"^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
        r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
        r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
        r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    )

    return re.match(ipv4_pattern, ip_address) is not None


def setup_logger(
    name: str, level=logging.INFO, log_file: str = None, file_mode: str = "a"
) -> logging.Logger:
    """Set up a logger with the specified name, level, file name, and file mode."""

    logger = logging.getLogger(name)
    logger.setLevel(level)

    for h in logger.handlers[:]:
        logger.removeHandler(h)

    ch = logging.StreamHandler()
    ch.setLevel(level)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    if log_file:
        fh = logging.FileHandler(log_file, mode=file_mode)
        fh.setLevel(level)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger
