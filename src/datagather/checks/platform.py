#!/usr/bin/env python3
import platform


def run():
    '''
    Gather basic platform information.

    Provides:

    .. code-block:: python

        'platform_host': str
        'platform_arch': str
        'platform_kernel_rel': str
        'platform_kernel_type': str
    '''
    devinfo = platform.uname()
    return {
        'platform_host': devinfo.node,
        'platform_arch': devinfo.machine,
        'platform_kernel_rel': devinfo.release,
        'platform_kernel_type': devinfo.system,
    }
