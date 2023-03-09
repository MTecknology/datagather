#!/usr/bin/env python3
'''
DataGather (main application)
'''
# Python imports
import json

# Application imports
from datagather import checks, loggers, runtime


def main():
    '''
    Run all configured checks and report gathered data.
    '''
    # Load runtime
    opts = runtime.OptsParser().parse_opts()
    conf = runtime.ConfigParser(opts.config)

    # Gather device data
    results = {}
    for check in conf.checks:
        checkopts = conf['checkargs'].get(check, {})
        results = {**results, **checks.run(check, checkopts)}

    # Report gathered data
    if opts.logger:
        logopts = json.loads(opts.logopts)
        loggers.send(opts.logger, logopts, results)
    else:
        for logger, logopts in conf.loggers.items():
            loggers.send(logger, logopts, results)


if __name__ == '__main__':
    main()
