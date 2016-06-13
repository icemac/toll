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


[commands]
==========

This section contains the commands which can be run using `toll`.

Example::

    [commands]
    build = bin/buildout -n
    test = bin/py.test
