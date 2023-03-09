#!/usr/bin/env python3
'''
Run unit tests for df checks.
'''
# DG imports
import datagather.checks.df


def test_run_defaults():
    result = datagather.checks.df.run()
    assert isinstance(result, dict)
    assert len(result) == 3
    assert isinstance(result['df_total-/'], int)
