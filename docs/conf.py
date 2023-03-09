#!/usr/bin/env python3
import os
import sys


def setup(app):
    os.system(os.path.realpath(__file__).replace('/conf.py', '/genstubs'))


# DG Path
sys.path.insert(0, os.path.abspath('../src'))

# Documentation Settings
project = 'Data Gather'
copyright = '2023, Michael Lustfield'  # pylint: disable=W0622
author = 'Michael Lustfield'
release = '0.0.0'
extensions = []
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
extensions = ['sphinx.ext.autodoc', 'sphinxarg.ext']
