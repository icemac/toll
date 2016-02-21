==========
About toll
==========

toll = **t**\ est **o**\ ffline **l**\ ightweight **l**\ ocally — poor man's integration testing:

* run the tests of multiple configured packages:
    * right one after another
    * stopping with the first package which has a broken test

This package is compatible with Python version 3.5.

.. contents::

Requirements
============

* The packages for test have to be checked out and build beforehand.
* The test runners of the packages have to be called with an identical call.

Usage
=====

Installation
------------

Install it as usual using pip::

    $ pip install toll

Config file
-----------

You need an ini style config file. Example contents::

    [packages]
    my.package.one
    my.package.two

    [commands]
    test = bin/py.test

The complete list of possible config file contents is in the documentation on
http://pythonhosted.org/toll/config.html.

Run it
------

Run it using::

    $ toll config.ini

For other options see::

    $ toll --help
