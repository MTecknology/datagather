#!/usr/bin/env python3
'''
A basic output option intended for debugging.
'''
import pprint


def send(payload):
    '''
    Send gathered data to json file.
    '''
    pprint.pprint(payload)
