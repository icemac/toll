from .config import parsed_file, packages, commands, Command
import pytest


EXAMPLE_CONFIG = """\
[upload]
precondition = test -e upload.py
command = bin/python upload.py

[test]
command = bin/py.test

[run]
command = bin/run

[run-through]
ignore-exit-code = true
command = bin/run

[packages]
foo.a
bar.x"""


@pytest.fixture('function')
def config_file(tmpdir):
    """Create a config file with the given content."""
    def config(content=EXAMPLE_CONFIG):
        data = tmpdir.join('config.ini')
        data.write(content)
        return parsed_file(data.open())
    return config


def test_config__packages__2(config_file):
    """It raises a RuntimeError if the [packages] section is missing."""
    with pytest.raises(RuntimeError) as err:
        packages(config_file('[test]\ncommand=bin/test'))
    assert ('Missing the section [packages] in the config file.' ==
            str(err.value))


def test_config__commands__1(config_file):
    """It returns the selected commands from the config file."""
    assert ((Command('bin/py.test'),
             Command('bin/python upload.py',
                     precondition='test -e upload.py'),
             Command('bin/run', ignore_exit_code=True)) ==
            commands(config_file(), ['test', 'upload', 'run-through']))


def test_config__commands__3(config_file):
    """It raises a `RuntimeError` if a requested command is missing."""
    file = config_file()
    with pytest.raises(RuntimeError) as err:
        commands(file, ['run', 'stop'])
    assert ("Section [commands] in the config file does not contain the key "
            "'stop' you requested to execute." ==
            str(err.value))


def test_config__Command____repr____1():
    """It contains the name of the wrapped command."""
    cmd = Command('bin/test -v')
    assert "<Command 'bin/test -v'>" == repr(cmd)


def test_config__Command____repr____2():
    """It contains the name of the precondition."""
    cmd = Command('bin/test -v', 'test -e bin/test', ignore_exit_code=True)
    assert ("<Command 'bin/test -v' if 'test -e bin/test' ignore-exit-code>" ==
            repr(cmd))


def test_config__Command____eq____1():
    """It is equal to an identical command."""
    cmd1 = Command('bin/test')
    cmd2 = Command('bin/test')
    assert cmd1 == cmd2


def test_config__Command____ne____1():
    """It is not equal to a command with a different command."""
    cmd1 = Command('bin/test1', precondition='test -e bin/test')
    cmd2 = Command('bin/test2', precondition='test -e bin/test')
    assert cmd1 != cmd2


def test_config__Command____ne____2():
    """It is not equal to a command with a different precondition."""
    cmd1 = Command('bin/test')
    cmd2 = Command('bin/test', precondition='test -e bin/test')
    assert cmd1 != cmd2


def test_config__Command____ne____2_5():
    """It is not equal to a command with a different ignore-exit-code."""
    cmd1 = Command('bin/test')
    cmd2 = Command('bin/test', ignore_exit_code=True)
    assert cmd1 != cmd2


def test_config__Command____ne____3():
    """It is not equal to something which is not a command."""
    cmd = Command('bin/test')
    assert cmd != 'bin/test'
