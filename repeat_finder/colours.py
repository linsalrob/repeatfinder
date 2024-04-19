"""
Colors that you can import and make the text look pretty

Source: https://stackoverflow.com/questions/287871/print-in-terminal-with-colors
"""
import os
import sys
from .rob_error import ColorNotFoundError

__author__ = 'Rob Edwards'

class Colours():
    """
    Some colours to make things pretty
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    PINK = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[0m'

def message(msg, color):
    """
    Print a message to stderr using color
    :param msg: the message to print
    :param color: the color to use
    :return: nothing
    """

    color = color.upper()
    if color not in colors.color:
        raise ColorNotFoundError(f"There is no color {color}")

    if os.fstat(0) == os.fstat(1):
        #  stderr is not redirected
        sys.stderr.write(f"{colors.color[color]}{msg}{colors.color['ENDC']}\n")
    else:
        sys.stderr.write(f"{msg}\n")
