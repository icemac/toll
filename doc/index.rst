=====================================
toll — poor man's integration testing
=====================================

toll = **t**\ est **o**\ ffline **l**\ ocally **l**\ ightweight

Run the tests of multiple configured packages:

* right one package after another

* stopping with the first package which has a failing test

.. raw:: html

    <p><a href="https://commons.wikimedia.org/wiki/File:Schranke_fast_oben.svg#/media/File:Schranke_fast_oben.svg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Schranke_fast_oben.svg/1200px-Schranke_fast_oben.svg.png" alt="Schranke fast oben.svg"></a><br>By <a href="//commons.wikimedia.org/wiki/User:MichaelFrey" title="User:MichaelFrey">MichaelFrey</a> (<a href="//commons.wikimedia.org/wiki/User_talk:MichaelFrey" title="User talk:MichaelFrey"><span class="signature-talk">talk</span></a>) - <span class="int-own-work" lang="en">Own work</span>, <a href="http://creativecommons.org/licenses/by/3.0" title="Creative Commons Attribution 3.0">CC BY 3.0</a>, https://commons.wikimedia.org/w/index.php?curid=7932305</p>


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

You need an ini style config file. Example contents of a file named
`config.ini`::

    [packages]
    my.package.one
    my.package.two

    [commands]
    test = bin/py.test

For the complete list of possible config options see the section :doc:`config`.

Run it
------

Run it using::

    $ toll config.ini

For other options see::

    $ toll --help


Other topics
============

.. toctree::
    :maxdepth: 1

    config
    about
    changes
