#!/usr/bin/env python3
import datagather.tools


def run():
    '''
    Gather current memory information.

    Provides:

    .. code-block:: python

        'memory_total': str
        'memory_used': str
        'memory_free': str
        'memory_active': str
    '''
    meminfo = datagather.tools.FileKV('/proc/meminfo')
    return {
        'memory_total': meminfo['MemTotal'],
        'memory_used': meminfo['MemAvailable'],
        'memory_free': meminfo['MemFree'],
        'memory_active': meminfo['Active'],
    }
