"""
A class to hold the parameters for our repeat search
"""

__author__ = 'Rob Edwards'


class RepeatSearch():
    """
    A repeat search class that allows us to pass data around conveniently
    """

    def __init__(self, fastafile, minlen, gaplen, output):
        self.fastafile = fastafile
        self.minlen = minlen
        self.gaplen = gaplen
        self.output = output
        self.dnaseq = None
        self.dnaseqid = None

    def set_dna_sequence(seqid, sequence):
        self.dnaseqid = seqid
        self.dnaseq = sequence

    def get_dna_sequence():
        return self.dnaseq

    def get_seqid():
        return self.dnaseqid

