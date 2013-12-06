"""
Application that optimizes large ordered data set retrieving when using MySql.
"""

VERSION = (1, 1, 0)


def get_version():
    """Returns the version as a string."""
    return '.'.join(map(str, VERSION))