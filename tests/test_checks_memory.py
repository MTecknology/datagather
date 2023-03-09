#!/usr/bin/env python3
'''
Run unit tests for memory checks.
'''
# DG imports
import datagather.checks.memory


def test_run_defaults():
    result = datagather.checks.memory.run()
    assert isinstance(result, dict)
    assert isinstance(result['memory_total'], str)
    assert isinstance(result['memory_used'], str)
    assert isinstance(result['memory_free'], str)
    assert 'kB' in result['memory_total']
