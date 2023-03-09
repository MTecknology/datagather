#!/usr/bin/env python3
'''
Run unit tests for memory checks.
'''
# DG imports
import datagather.checks.cpu


def test_run_defaults():
    result = datagather.checks.cpu.run()
    assert isinstance(result, dict)
    assert isinstance(result['cpu_10min'], float)
