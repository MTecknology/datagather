Runtime
=======

.. automodule:: datagather.runtime

.. _commandline:

Command Line Usage
------------------

.. autoclass:: datagather.runtime.OptsParser

    .. argparse::
       :module: datagather.runtime
       :func: _optsparser
       :prog: datagather
       :nodefault:

.. _configuration:

Configuration File
------------------

.. autoclass:: datagather.runtime.ConfigParser

Example Configuration
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

    {
        "checks": ["platform", "cpu", "df", "memory"],
        "checkargs": {
            "df": {
                "fslist": ["/", "/tmp", "/boot", "/var"]
            },
            "users": {
                "uidlist": [1000, 1001],
                "namelist": ["jim", "bob", "timmy"]
            }
        },
        "loggers": {
            "json": {},
            "elkbeat": {
                "host": "elk.domain.tld",
                "token": "abc123"
            }
        }
    }

Default Configuration
~~~~~~~~~~~~~~~~~~~~~

.. autoattribute:: datagather.runtime.DEFAULTS

Default Location: ``/etc/datagather.json``:
