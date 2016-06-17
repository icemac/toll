try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # noqa

try:
    from unittest import mock
except ImportError:
    try:
        import mock  # noqa
    except ImportError:
        pass
