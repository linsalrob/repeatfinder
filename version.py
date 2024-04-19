"""
Get the version number for the scripts
"""

import os

__version__ = "0.0.0 (probably not installed from pip?)"

vfile = os.path.join(os.path.dirname(os.path.realpath(__file__)), "_version.py")

if os.path.exists(vfile):
    with open(vfile, "r", encoding='utf-8') as vf:
        __version__ = vf.read().strip()
