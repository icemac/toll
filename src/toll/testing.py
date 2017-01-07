from .config import Command
import os.path
import pkg_resources
import re
import sys

raw_test_command = '{0.executable} setup.py -q test'.format(sys)
test_command = Command(raw_test_command)


def get_packages(*names):
    """Get relative package path.

    We use paths relative to the package name to be able to test os.chdir
    calls.
    """
    base_path = "{0}{1.sep}".format(os.getcwd(), os)
    return [
        pkg_resources.resource_filename(
            'toll', 'fixtures/{}'.format(x)).replace(base_path, '')
        for x in names]


def remove_ansi_codes(text):
    """Remove ANSI colour codes from text."""
    ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
    return ansi_escape.sub('', text)
