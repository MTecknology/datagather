#!/usr/bin/env python3
import shutil


def run(fslist=['/']):
    '''
    Gathers disk usage information for mounted file systems.

    fslist
        List of file system paths to scan.

    Provides:

    .. code-block:: python

        'df_total-{fs}': int
        'df_used-{fs}': int
        'df_free-{fs}': int
    '''
    stats = {}
    for path in fslist:
        stat = shutil.disk_usage(path)
        stats[f'df_total-{path}'] = stat.total
        stats[f'df_used-{path}'] = stat.used
        stats[f'df_free-{path}'] = stat.free
    return stats
