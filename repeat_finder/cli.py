"""

"""

import os
import sys
import argparse
import PyRepeatFinder
from .sequences import stream_fasta

__author__ = 'Rob Edwards'


def 


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=' ')
    parser.add_argument('-f', help='fasta file of DNA sequences', required=True)
    parser.add_argument('-m', help='minimum repeat length', type=int, default=11)
    parser.add_argument('-v', help='verbose output', action='store_true')
    args = parser.parse_args()



