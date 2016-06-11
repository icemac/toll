from .testing import get_packages, test_command
from .run import Runner


def test_run____call____1():
    """It returns `True` on success of all packages."""
    runner = Runner(test_command, get_packages('fine', 'finetoo'))
    assert True is runner()


def test_run____call____2(capsys):
    """It prints the tests results to stdout."""
    packages = get_packages('fine', 'finetoo')
    runner = Runner(test_command, packages)
    runner()
    out, err = capsys.readouterr()
    assert 'Testing {}'.format(packages[0]) in out
    assert 'Testing {}'.format(packages[1]) in out
    assert out.strip().endswith('SUCCESS :-)')


def test_run____call____3(capsys):
    """It stops after the first package with a failure."""
    packages = get_packages('bad', 'fine')
    runner = Runner(test_command, packages)
    runner()
    out, err = capsys.readouterr()
    assert 'Testing {}'.format(packages[0]) in out
    assert 'Testing {}'.format(packages[1]) not in out
    assert out.strip().endswith('FAILURE :-(')
