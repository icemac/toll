from .run import Runner
from .testing import get_packages, test_command
import re
import sys


def test_run____call____1():
    """It returns `True` on success of all packages."""
    runner = Runner([test_command], get_packages('fine', 'finetoo'))
    assert True is runner()


def test_run____call____2(capsys):
    """It prints the tests results to stdout."""
    packages = get_packages('fine', 'finetoo')
    runner = Runner([test_command], packages)
    runner()
    out, err = capsys.readouterr()
    assert 'Running {0} on {1[0]}'.format(test_command, packages) in out
    assert 'Running {0} on {1[1]}'.format(test_command, packages) in out
    assert out.strip().endswith('SUCCESS :-)')


def test_run____call____3(capsys):
    """It stops after the first package with a failure."""
    packages = get_packages('bad', 'fine')
    runner = Runner([test_command], packages)
    runner()
    out, err = capsys.readouterr()
    assert 'Running {0} on {1[0]}'.format(test_command, packages) in out
    assert 'Running {0} on {1[1]}'.format(test_command, packages) not in out
    assert out.strip().endswith('FAILURE :-(')


def test_run____call____4(capsys):
    """It runs multiple commands on each package."""
    packages = get_packages('fine', 'finetoo')
    runner = Runner([test_command, sys.executable], packages)
    runner()
    out, err = capsys.readouterr()
    assert ("""\
Running {0} on {2[0]}
Running {0} on {2[1]}
Running {1} on {2[0]}
Running {1} on {2[1]}""".format(test_command, sys.executable, packages) ==
            "\n".join(re.findall('^Running .* on .*$', out, re.M)))
    assert out.strip().endswith('SUCCESS :-)')
