#!/usr/bin/env python3
import os


def run():
    '''
    Gathers CPU load averages.

    Provides:

    .. code-block:: python

        'cpu_5min': float
        'cpu_10min': float
        'cpu_15min': float
    '''
    loadavg = os.getloadavg()
    return {
        'cpu_5min': loadavg[0],
        'cpu_10min': loadavg[1],
        'cpu_15min': loadavg[2],
    }
