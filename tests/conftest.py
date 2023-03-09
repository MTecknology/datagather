#!/usr/bin/env python3
import pytest
import os
import tempfile


@pytest.fixture
def tempconfig():
    '''
    Create a temporary file, yield path, and delete on exit.
    '''
    try:
        f = tempfile.NamedTemporaryFile(delete=False)
        tmp_name = f.name
        f.close()
        yield tmp_name
    finally:
        os.unlink(tmp_name)
