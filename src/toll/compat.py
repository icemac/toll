try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # noqa

try:
    from unittest import mock
except ImportError:
    import mock   # noqa
