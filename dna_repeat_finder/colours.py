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

    colour = {
        'HEADER': '\033[95m',
        'OKBLUE': '\033[94m',
        'OKGREEN': '\033[92m',
        'WARNING': '\033[93m',
        'FAIL': '\033[91m',
        'ENDC': '\033[0m',
        'BOLD': '\033[1m',
        'UNDERLINE': '\033[4m',
        'PINK': '\033[95m',
        'BLUE': '\033[94m',
        'GREEN': '\033[92m',
        'YELLOW': '\033[93m',
        'RED': '\033[91m',
        'WHITE': '\033[0m',
    }

    def get(self, col):
        """
        get a colour
        """
        return self.colour[col] if col in self.colour else self.colour['WHITE']

    def set(self, name, val):
        """
        set a colour
        """
        self.colour[name] = val


def message(msg, color):
    """
    Print a message to stderr using color
    :param msg: the message to print
    :param color: the color to use
    :return: nothing
    """

    color = color.upper()
    if color not in Colours.colour:
        raise ColorNotFoundError(f"There is no colour {color}")

    if os.fstat(0) == os.fstat(1):
        #  stderr is not redirected
        sys.stderr.write(f"{Colours.colour[color]}{msg}{Colours.colour['ENDC']}\n")
    else:
        sys.stderr.write(f"{msg}\n")
