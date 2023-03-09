#!/usr/bin/env python3
'''
Simple utilities to help gather data.
'''


class FileKV(object):
    '''
    Reads a delimited file into key-value pairs.
    '''

    def __init__(self, path, delim=':'):
        self._path = path
        self._delim = delim
        with open(path) as f:
            d = dict(x.strip().split(None, 1) for x in f)
            d = {key.strip(delim): item.strip() for key, item in d.items()}
        self._data = d

    def __getitem__(self, key):
        return self._data[key]
