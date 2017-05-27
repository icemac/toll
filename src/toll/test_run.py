from .config import Command
from .run import Runner
from .testing import get_packages, test_command, raw_test_command
from .testing import remove_ansi_codes
import re
import sys


def test_run__Runner____call____1():
    """It returns `True` on success of all packages."""
    runner = Runner([test_command], get_packages('fine', 'finetoo'))
    assert True is runner()


def test_run__Runner____call____2(capsys):
    """It prints the tests results to stdout."""
    pkgs = get_packages('fine', 'finetoo')
    runner = Runner([test_command], pkgs)
    runner()
    out, err = capsys.readouterr()
    out = remove_ansi_codes(out)
    assert 'Running {0} on {1[0]}'.format(raw_test_command, pkgs) in out
    assert 'Running {0} on {1[1]}'.format(raw_test_command, pkgs) in out
    assert out.strip().endswith('SUCCESS :-)')


def test_run__Runner____call____3(capsys):
    """It stops after the first package with a failure."""
    pkgs = get_packages('bad', 'fine')
    runner = Runner([test_command], pkgs)
    runner()
    out, err = capsys.readouterr()
    out = remove_ansi_codes(out)
    assert 'Running {0} on {1[0]}'.format(raw_test_command, pkgs) in out
    assert 'Running {0} on {1[1]}'.format(raw_test_command, pkgs) not in out
    assert out.strip().endswith('FAILURE :-(')


def test_run__Runner____call____4(capsys):
    """It runs multiple commands on each package."""
    pkgs = get_packages('fine', 'finetoo')
    runner = Runner([test_command, Command(sys.executable)], pkgs)
    runner()
    out, err = capsys.readouterr()
    out = remove_ansi_codes(out)
    assert ("""\
Running {0} on {2[0]}
Running {0} on {2[1]}
Running {1} on {2[0]}
Running {1} on {2[1]}""".format(raw_test_command, sys.executable, pkgs) ==
            "\n".join(re.findall('^Running .* on .*$', out, re.M)))
    assert out.strip().endswith('SUCCESS :-)')


def test_run__Runner____call____5(capsys):
    """It omits the command run if the precondition is not met."""
    pkgs = get_packages('bad', 'fine')
    precondition = 'test -e fine.py'
    runner = Runner([Command(raw_test_command, precondition)], pkgs)
    runner()
    out, err = capsys.readouterr()
    out = remove_ansi_codes(out)
    assert out.strip().endswith('SUCCESS :-)')
    assert 'Not running {0} on {1[0]}'.format(raw_test_command, pkgs) in out
    assert 'Precondition {0} on {1[0]} not met.'.format(
        precondition, pkgs) in out
    assert 'Running {0} on {1[1]}'.format(raw_test_command, pkgs) in out


def test_run__Runner____call____6(capsys):
    """It does not stop if ignore_exit_code is set."""
    pkgs = get_packages('bad', 'fine')
    runner = Runner([Command(raw_test_command, ignore_exit_code=True)], pkgs)
    runner()
    out, err = capsys.readouterr()
    out = remove_ansi_codes(out)
    assert 'Running {0} on {1[0]}'.format(raw_test_command, pkgs) in out
    assert 'Running {0} on {1[1]}'.format(raw_test_command, pkgs) in out
    assert out.strip().endswith('SUCCESS :-)')
