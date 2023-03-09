#!/usr/bin/env python3
'''
Provides basic interfaces to collect runtime configuration.
'''
import argparse
import json
import os


# Application Defaults
DEFAULTS = {
    # Enabled Checks
    'checks': [
        'platform',
        'cpu',
        'memory',
    ],
    # Check Arguments
    'checkargs': {},
    # Loggers Configuration
    'loggers': {
        'json': {},
    },
}


class OptsParser(object):
    '''
    Collect arguments passed to script.
    '''

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            usage='datagather [-h] <optional arguments>',
            formatter_class=lambda prog: argparse.HelpFormatter(
                prog,
                width=100))
        self._main_opts()

    def parse_opts(self):
        '''
        Return parsed options
        '''
        return self.parser.parse_args()

    def _main_opts(self):
        '''
        Add available arguments to argparse instance
        '''
        self.parser.add_argument(
            '-v', '--verbose',
            dest='verbose',
            action='store_true',
            help='Use verbose logging')
        self.parser.add_argument(
            '-c', '--config',
            dest='config',
            action='store',
            metavar='X',
            help='Configuration file (default: /etc/datagather.json)',
            default='/etc/datagather.json')
        self.parser.add_argument(
            '-l', '--logger',
            dest='logger',
            action='store',
            metavar='X',
            help='Override configured output',
            default=None)
        self.parser.add_argument(
            '-o', '--logopts',
            dest='logopts',
            action='store',
            metavar='X',
            help='Options provided to logger (default: {})',
            default='{}')


def _optsparser():
    '''TODO: Quick hack to make sphinx-argparse work.'''
    return OptsParser().parser


class ConfigParser(object):
    '''
    Data gathering is driven by the ``configuration file``.

    checks (list):
        List of ref:`checks` to run during data collection

    checkargs (dict):
        Configuration arguments for each check

    loggers (dict):
        Destination (and configuration) for collected data.
    '''

    def __init__(self, config_path='/etc/datagather.json'):
        self.config_path = config_path
        self.data = DEFAULTS
        if os.path.exists(config_path):
            self.load()

    def __getattr__(self, key, default=None):
        '''
        Return a single top-level configuration item.
        '''
        return self.data.get(key, default)

    def load(self):
        '''
        Load yaml data into parser.
        '''
        with open(self.config_path) as fh:
            confdata = json.load(fh)
        self.data = {**DEFAULTS, **confdata}
