#!/usr/bin/env python3
'''
Checks are managed by the :ref:`Configuration File <configuration>`. Checks can
be enabled by adding the check name to the ``checks`` list. Checks which support
additional arguments can be configured using the ``checkargs`` dictionary.

Example Config
    This configuration enables the ``df`` and ``cpu`` checks, configuring df to
    collect information from three paths:

    .. code-block:: json

        {
            "checks": ["cpu", "df"],
            "checkargs": {
                "df": {"fslist": ["/", "/boot", "/var"]}
            }
        }
'''
import importlib


def run(check, checkopts):
    '''
    Load and execute a specified check.
    '''
    mod = importlib.import_module('datagather.checks.{}'.format(check))
    results = mod.run(**checkopts)
    return results
