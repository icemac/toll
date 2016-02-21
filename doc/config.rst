===========
Config file
===========

There can be several sections in the config file. They are described here.

[packages]
==========

This section contains a list of relative paths of packages which should be
tested.


[commands]
==========

This section contains the commands which can be run using toll.

test
----

This configures the test command run inside each package. Example::

    [commands]
    test = bin/py.test
