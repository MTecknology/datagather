#!/usr/bin/env python3
'''
Loggers are used to ship gathered data to useful location. Unlike checks, logger
arguments are :ref:`configured <configuration>` with the logger setting.

Example Config
    This configuration enables two loggers, providing one with no arguments.

    .. code-block:: json

        {
            "loggers": {
                "pprint": {},
                "elkbeat": {
                    "host": "elk.domain.tld",
                    "token": "hunter12"
                }
            }
        }
'''
import importlib


def send(logger, logopts, payload):
    '''
    Load and execute a specified check.
    '''
    mod = importlib.import_module('datagather.loggers.{}'.format(logger))
    results = mod.send(payload, **logopts)
    return results
