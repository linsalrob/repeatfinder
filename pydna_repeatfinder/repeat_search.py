"""
A class to hold the parameters for our repeat search
"""

__author__ = 'Rob Edwards'


class RepeatSearch:
    """
    A repeat search class that allows us to pass data around conveniently
    """

    def __init__(self, fastafile, minlen, gaplen, output):
        self.fastafile = fastafile
        self.minlen = minlen
        self.gaplen = gaplen
        self.output = output
        self._dnaseq = None
        self._seqid = None

    def set_dna_sequence(self, seqid: str, sequence: str) -> None:
        """
        Set the object's DNA sequence and ID
        :param seqid: the sequence ID
        :param sequence: the DNA sequence
        """
        self._seqid = seqid
        self._dnaseq = sequence

    @property
    def dnaseq(self) -> str:
        """
        Get the DNA sequence
        :return: the DNA sequence
        """
        return self._dnaseq

    @dnaseq.setter
    def dnaseq(self, dnaseq: str) -> None:
        """
        Set the object's DNA sequence'
        :param dnaseq: the dna sequence
        """
        self._dnaseq = dnaseq

    @property
    def seqid(self):
        """
        Get the sequence id
        :return: the sequence id
        """
        return self._seqid

    @seqid.setter
    def seqid(self, seqid: str) -> None:
        """
        Set the sequence id
        :param seqid: the sequence id
        """
        self._seqid = seqid
