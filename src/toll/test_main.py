from .main import main
from unittest.mock import patch


def test_main__main__1():
    """It feeds the file handle of the config file into the Configuration."""
    with patch('toll.main.Configuration') as Configuration:
        main(['selftest.ini'])
    assert Configuration.called
    assert 'selftest.ini' == Configuration.call_args[0][0].name
