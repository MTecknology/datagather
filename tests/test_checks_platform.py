#!/usr/bin/env python3
'''
Run unit tests for memory checks.
'''
# DG imports
import datagather.checks.platform


def test_run_defaults():
    result = datagather.checks.platform.run()
    assert isinstance(result, dict)
    assert isinstance(result['platform_host'], str)
