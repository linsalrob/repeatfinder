"""
A class to hold the parameters for our repeat search
"""

__author__ = 'Rob Edwards'


class RepeatSearch():
    def __init__(self, fastafile, minlen, gaplen, output):
        self.fastafile = fastafile
        self.minlen = minlen
        self.gaplen = gaplen
        self.output = output
        self.dnaseq = None
        self.dnaseqid = None

    

    

