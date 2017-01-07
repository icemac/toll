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

try:
    from shutil import get_terminal_size
except ImportError:
    from backports.shutil_get_terminal_size import get_terminal_size  # noqa
