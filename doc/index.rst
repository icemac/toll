=====================================
toll — poor man's integration testing
=====================================

toll = **t**\ est **o**\ ffline **l**\ ocally **l**\ ightweight

Run commands on multiple configured packages:

* Commands can be set-up steps or a call to the test runner etc.

* Each command is run on each package.

* It stops if a command exits with a non-zero exit code (aka an error).

.. raw:: html

    <p><a href="https://commons.wikimedia.org/wiki/File:Schranke_fast_oben.svg#/media/File:Schranke_fast_oben.svg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Schranke_fast_oben.svg/1200px-Schranke_fast_oben.svg.png" alt="Schranke fast oben.svg"></a><br>By <a href="//commons.wikimedia.org/wiki/User:MichaelFrey" title="User:MichaelFrey">MichaelFrey</a> (<a href="//commons.wikimedia.org/wiki/User_talk:MichaelFrey" title="User talk:MichaelFrey"><span class="signature-talk">talk</span></a>) - <span class="int-own-work" lang="en">Own work</span>, <a href="http://creativecommons.org/licenses/by/3.0" title="Creative Commons Attribution 3.0">CC BY 3.0</a>, https://commons.wikimedia.org/w/index.php?curid=7932305</p>


Requirements
============

* The packages have to be checked out beforehand.
* Currently the commands have to be identical across all packages.

Usage
=====

Installation
------------

Install it as usual using pip::

    $ pip install toll

Config file
-----------

You need an ini style config file. Its name should be `toll.ini`. Here
are example contents of such a file.::

    [packages]
    my.package.one
    my.package.two

    [commands]
    test = bin/py.test
    build = bin/buildout -n

For the complete list of possible configuration options see the
section :doc:`config`.

Run it
------

By default the command named ``test`` from the config file is run::

    $ toll

If you specify multiple commands each one is run on each package before
proceeding to the next command::

    $ toll build test

For other options see::

    $ toll --help


Other topics
============

.. toctree::
    :maxdepth: 1

    config
    about
    changes
