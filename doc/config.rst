===========
Config file
===========

There can be the following sections in the config file:

[packages]
==========

This section contains a list of relative paths of packages. They are used to
run commands on them.

Example::

    [packages]
    ../foo.bar
    pkgs/baz


[<command-name>]
================

All sections besides ``[packages]`` are treated as commands.

Required parameters
-------------------

* ``command`` - command to be run


Optional parameters
-------------------

* ``precondition`` - do not run the command if the precondition is not met aka
  ``the command returns a non-zero exit code.

Example
-------

This a an example of some commands::

    [build]
    precondition = test -e bin/buildout
    command = bin/buildout -n

    [test]
    command = bin/py.test

The precondition of ``[build]`` checks whether ``bin/buildout`` exists as the
command would fail if not.
