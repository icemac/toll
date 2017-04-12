===============
Developing toll
===============

:Author:
    Michael Howitz <icemac@gmx.net>

:Documentation:
    http://toll.readthedocs.io

:PyPI page:
    https://pypi.org/project/toll/

:Issues:
    https://github.com/icemac/toll/issues

:Source code:
    https://github.com/icemac/toll

:Change log:
    https://raw.githubusercontent.com/icemac/toll/master/CHANGES.rst

Run the tests
=============

Install tox_ as the test runner and the call it to run the tests::

    $ tox

To run the tests of `toll` using `toll` itself call::

    $ python3.5 bootstrap.py
    $ bin/buildout
    $ bin/toll

.. _tox : http://tox.readthedocs.io/en/latest/install.html
