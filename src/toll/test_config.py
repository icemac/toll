from .config import parsed_file, commands
import pytest


EXAMPLE_CONFIG = """\
[commands]
upload = bin/python upload.py
test = bin/py.test
run = bin/run
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


def test_config__commands__1(config_file):
    """It returns the selected commands from the config file."""
    assert (('bin/py.test', 'bin/python upload.py') ==
            commands(config_file(), ['test', 'upload']))


def test_config__commands__2(config_file):
    """It raises a `RuntimeError` if the commands section is missing."""
    file = config_file("")
    with pytest.raises(RuntimeError) as err:
        commands(file, [])
    assert ('Missing the section [commands] in the config file.' ==
            str(err.value))


def test_config__commands__3(config_file):
    """It raises a `RuntimeError` if a requested command is missing."""
    file = config_file()
    with pytest.raises(RuntimeError) as err:
        commands(file, ['run', 'stop'])
    assert ("Section [commands] in the config file does not contain the key "
            "'stop' you requested to execute." ==
            str(err.value))
