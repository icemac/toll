from .config import Configuration
import pytest


@pytest.fixture('function')
def config(tmpdir):
    """Create a config file with the given content."""
    def config(content):
        data = tmpdir.join('config.ini')
        data.write(content)
        return data.open()
    return config


def test_config__Configuration____init____1(config):
    """It stores the commands and packages."""
    file = config("""\
[commands]
test = bin/py.test
[packages]
foo.a
bar.x""")
    config = Configuration(file)
    assert {'test': 'bin/py.test'} == dict(config.commands)
    assert ['foo.a', 'bar.x'] == config.packages


def test_config__Configuration___extract_commands__1(config):
    """It raises a `RuntimeError` if the commands section is missing."""
    file = config("")
    with pytest.raises(RuntimeError) as err:
        Configuration(file)
    assert ('Missing the section [commands] in the config file.' ==
            str(err.value))


def test_config__Configuration___extract_commands__2(config):
    """It raises a `RuntimeError` if the test command is missing."""
    file = config("[commands]")
    with pytest.raises(RuntimeError) as err:
        Configuration(file)
    assert ('Section [commands] in the config file does not contain the key '
            '"test" which is needed to define the test command.' ==
            str(err.value))
