#!/usr/bin/env python3
'''
Test application runtime. This is closer to an "integration test."
'''
# Python imports
import sys
import unittest.mock

# DG imports
import datagather.runtime
import datagather.checks


def test_opts_present(tempconfig):
    '''
    Verify parameters can be parsed.
    '''
    with open(tempconfig, 'w') as fh:
        fh.write('{}\n')

    testargs = ['datagather', '-c', tempconfig]
    with unittest.mock.patch.object(sys, 'argv', testargs):
        opts = datagather.runtime.OptsParser().parse_opts()
        assert opts is not None


def test_run_json(tempconfig):
    '''
    Verify an empty config file results in correct defaults.
    '''
    with open(tempconfig, 'w') as fh:
        fh.write('{"checks": {"memory": {}}, "loggers": {"json": {}}}\n')

    results = {}
    testargs = ['datagather', '-c', tempconfig]
    with unittest.mock.patch.object(sys, 'argv', testargs):
        # COPY: __main__.py::main()
        opts = datagather.runtime.OptsParser().parse_opts()
        conf = datagather.runtime.ConfigParser(opts.config)
        for check, checkopts in conf.checks.items():
            results = {**results, **datagather.checks.run(check, checkopts)}
    assert results != {}
    assert isinstance(results['memory_free'], str)
