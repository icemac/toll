"""poor man's integration testing"""

from setuptools import setup, find_packages
import os.path
import shutil


def project_path(*names):
    """Path to a file in the project."""
    return os.path.join(os.path.dirname(__file__), *names)

test_require = [
    'pytest >= 3',
]

try:
    import unittest.mock  # noqa
except ImportError:
    test_require.append('mock')

install_requires = [
    'colorama',
]

if not hasattr(shutil, 'get_terminal_size'):
    install_requires.append('backports.shutil_get_terminal_size')

setup(
    name='toll',
    version='4.0',
    install_requires=install_requires,
    extras_require={
        'test': test_require,
    },

    entry_points={
        'console_scripts': [
            'toll = toll.main:main'
        ],
    },

    author='Michael Howitz',
    author_email='icemac@gmx.net',
    license='MIT',
    url='https://github.com/icemac/toll',

    keywords='test testing offline integration multiple packages',
    classifiers="""\
Development Status :: 4 - Beta
Environment :: Console
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Natural Language :: English
Operating System :: OS Independent
Programming Language :: Python :: 2
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Programming Language :: Python :: Implementation :: CPython
Programming Language :: Python :: Implementation :: PyPy
Topic :: Software Development :: Testing
Topic :: Software Development :: Quality Assurance
Topic :: Utilities
"""[:-1].split('\n'),
    description=__doc__.strip(),
    long_description='\n\n'.join(open(project_path(name)).read() for name in (
        'README.rst',
        'CHANGES.rst',
    )),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
)
