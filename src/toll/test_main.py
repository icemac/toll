from .compat import mock
from .main import main
from .testing import get_packages, test_command
import os.path
import pytest
import re
import shutil


@pytest.fixture('function')
def toll_ini(tmpdir):
    """Get a factory to create a path to a toll.ini file."""
    def config_file(*package_names):
        package_paths = []
        for src in get_packages(*package_names):
            dest = str(tmpdir.join(os.path.basename(src)))
            shutil.copytree(src, dest)
            package_paths.append(dest)
        ini = tmpdir.join('toll-test.ini')
        ini.write('''\
[commands]
test = {test_command}
[packages]
{packages}
'''.format(test_command=test_command, packages='\n'.join(package_paths)))
        return str(ini)
    return config_file


def test_main__main__1(toll_ini, capsys):
    """It runs the test command by default."""
    config_path = toll_ini('fine', 'finetoo')
    main(['-c', config_path])
    out, err = capsys.readouterr()
    assert re.search('^Running .* setup.py -q test on .*/fine$', out, re.M)
    assert re.search('^Running .* setup.py -q test on .*/finetoo$', out, re.M)
    assert out.strip().endswith('SUCCESS :-)')


def test_main__main__2():
    """It defaults to `toll.ini` as the config file."""
    with mock.patch('toll.config.parsed_file') as parsed_file:
        try:
            main([])
        except RuntimeError:
            # toll.ini file is not valid but that's okay for the test
            pass
    assert 'toll.ini' == parsed_file.call_args[0][0].name
