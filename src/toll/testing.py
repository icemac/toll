import os.path
import pkg_resources
import sys


test_command = '{0.executable} setup.py -q test'.format(sys)


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
