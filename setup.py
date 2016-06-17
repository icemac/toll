"""poor man's integration testing"""

from setuptools import setup, find_packages
import glob
import os.path


def project_path(*names):
    """Path to a file in the project."""
    return os.path.join(os.path.dirname(__file__), *names)

test_require = []

try:
    import unittest.mock  # noqa
except ImportError:
    test_require.append('mock')


setup(
    name='toll',
    version='2.0',

    install_requires=[
    ],

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
    license='ZPL 2.1',
    url='https://bitbucket.org/icemac/toll/',

    keywords='test testing offline integration multiple packages',
    classifiers="""\
Development Status :: 4 - Beta
Environment :: Console
Intended Audience :: Developers
License :: OSI Approved
License :: OSI Approved :: Zope Public License
Natural Language :: English
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.5
Programming Language :: Python :: Implementation
Programming Language :: Python :: Implementation :: CPython
Topic :: Software Development
Topic :: Software Development :: Testing
Topic :: Software Development :: Quality Assurance
Topic :: Utilities
"""[:-1].split('\n'),
    description=__doc__.strip(),
    long_description='\n\n'.join(open(project_path(name)).read() for name in (
        'README.rst',
        'COPYRIGHT.txt',
        'CHANGES.rst',
    )),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    data_files=[('',
                 glob.glob(project_path('*.txt')),
                 glob.glob(project_path('*.rst')))],
    zip_safe=False,
)
