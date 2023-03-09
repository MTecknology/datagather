#!/usr/bin/env python3
'''
A basic output option intended for debugging.
'''
import json


def send(payload, path='/dev/stdout'):
    '''
    Send gathered data to json file.

    path
        Location to save json output.
    '''
    with open(path, 'w') as fh:
        json.dump(payload, fh)
