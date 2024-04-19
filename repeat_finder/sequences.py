import os
import sys
import gzip

import subprocess
from .rob_error import FastqFormatError
from .colours import colours, message

__author__ = 'Rob Edwards'


def stream_fastq(fqfile):
    """Read a fastq file and provide an iterable of the sequence ID, the
    full header, the sequence, and the quaity scores.

    Note that the sequence ID is the header up until the first space,
    while the header is the whole header.
    """

    if fqfile.endswith('.gz'):
        qin = gzip.open(fqfile, 'rt')
    else:
        qin = open(fqfile, 'r')

    linecounter = 0
    while True:
        header = qin.readline()
        linecounter += 1
        if not header:
            break
        if not header.startswith("@"):
            raise FastqFormatError(f"The file {fqfile} does not appear to be a four-line fastq file at line {linecounter}")
        header = header.strip()
        seqidparts = header.split(' ')
        seqid = seqidparts[0]
        seqid = seqid.replace('@', '')
        seq = qin.readline().strip()
        linecounter += 1
        qualheader = qin.readline()
        if not qualheader.startswith("+"):
            raise FastqFormatError(f"The file does not appear to be a four-line fastq file at line {linecounter}")
        linecounter += 1
        qualscores = qin.readline().strip()
        linecounter += 1
        header = header.replace('@', '', 1)
        if len(qualscores) != len(seq):
            raise FastqFormatError(f"The sequence and qual scores are not the same length at line {linecounter}")
        yield seqid, header, seq, qualscores




def stream_fasta(fastafile, whole_id=True):
    """
    Stream a fasta file, one read at a time. Saves memory!

    :param fastafile: The fasta file to stream
    :type fastafile: str
    :param whole_id: Whether to return the whole id (default) or just up to the first white space
    :type whole_id:bool
    :return:A single read
    :rtype:str, str
    """

    try:
        if fastafile.endswith('.gz'):
            f = gzip.open(fastafile, 'rt')
        elif fastafile.endswith('.lrz'):
            f = subprocess.Popen(['/usr/bin/lrunzip', '-q', '-d', '-f', '-o-', fastafile], stdout=subprocess.PIPE).stdout
        else:
            f = open(fastafile, 'r')
    except IOError as e:
        sys.stderr.write(str(e) + "\n")
        sys.stderr.write("Message: \n" + str(e.message) + "\n")
        sys.exit("Unable to open file " + fastafile)

    posn = 0
    while f:
        # first line should start with >
        idline = f.readline()
        if not idline:
            break
        if not idline.startswith('>'):
            sys.exit("Do not have a fasta file at: {}".format(idline))
        if not whole_id:
            idline = idline.split(" ")[0]
        idline = idline.strip().replace('>', '', 1)
        posn = f.tell()
        line = f.readline()
        seq = ""
        while not line.startswith('>'):
            seq += line.strip()
            posn = f.tell()
            line = f.readline()
            if not line:
                break
        f.seek(posn)
        yield idline, seq


def stream_gfa_sequences(gfafile):
    """
    Stream the sequences from a GFA file. At the moment we ignore the 
    rest of the information. This is not supposed to be a parser
    :param gfafile: the gfa file to read
    """

    try:
        if gfafile.endswith('.gz'):
            f = gzip.open(gfafile, 'rt')
        elif gfafile.endswith('.lrz'):
            f = subprocess.Popen(['/usr/bin/lrunzip', '-q', '-d', '-f', '-o-', gfafile], stdout=subprocess.PIPE).stdout
        else:
            f = open(gfafile, 'r')
    except IOError as e:
        sys.stderr.write(str(e) + "\n")
        sys.stderr.write("Message: \n" + str(e.message) + "\n")
        sys.exit("Unable to open file " + gfafile)

    while f:
        l = f.readline()
        if not l:
            break
        if not l.startswith("S"):
            continue
        p = l.strip().split("\t")
        yield p[1], p[2]


