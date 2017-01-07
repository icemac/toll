===============
Developing toll
===============

:Author:
    Michael Howitz <icemac@gmx.net>

:Documentation:
    http://toll.readthedocs.io

:PyPI page:
    https://pypi.python.org/pypi/toll

:Issues:
    https://bitbucket.org/icemac/toll/issues

:Source code:
    https://bitbucket.org/icemac/toll

:Change log:
    https://bitbucket.org/icemac/toll/raw/tip/CHANGES.rst

Run the tests
=============

Install the test runner and the `toll` script::

    $ python3.5 bootstrap.py
    $ bin/buildout

Call the test runner::

    $ bin/py.test

To run the tests of `toll` using `toll` itself call::

    $ bin/toll
