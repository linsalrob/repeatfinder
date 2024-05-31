"""
Command line invocations for find_repeats
"""

import sys
import argparse
from PyRepeatFinder import find_repeats
from .sequences import stream_fasta
from ._version import __version__

__author__ = 'Rob Edwards'

def find_dna_repeats(seqid, dna_seq, gap_len=0, min_len=0, verbose=False):
    """
    find the repeats in a dna sequence
    """

    if verbose:
        print(f"Finding repeats in {seqid} with seq {dna_seq}", file=sys.stderr)

    # if(!PyArg_ParseTuple(args, "siii", &dna, &gap_len, &output_rep_len, &debug))
    r = find_repeats(dna_seq, gap_len, min_len, 0)

    ## NOTE: The numbers returned by find_repeats are 1 indexed!!

    for rpt in r:
        if rpt['first_end'] > rpt['first_start']:
            start1 = rpt['first_start']-1
            rptlen1 = rpt['first_end']-rpt['first_start']
        else:
            start1 = rpt['first_end']-1
            rptlen1 = rpt['first_start']-rpt['first_end']

        if rpt['second_end'] > rpt['second_start']:
            start2 = rpt['second_start']-1
            rptlen2 = rpt['second_end']-rpt['second_start']
        else:
            start2 = rpt['second_end']-1
            rptlen2 = rpt['second_start']-rpt['second_end']

        seq1 = dna_seq[start1:start1+rptlen1]
        seq2 = dna_seq[start2:start2+rptlen2]
        data = [seqid, f"Number:{rpt['repeat_number']}", f"Len1:{rptlen1}",
                f"Len2:{rptlen2}",
                rpt['first_start'], rpt['first_end'],
                rpt['second_start'], rpt['second_end'],
                seq1, seq2
               ]
        print("\t".join(map(str, data)))


def repeats_in_fasta(fafile, gaplen, minlen, verbose=False):
    """
    Find all the repeats in the sequences in a fasta file
    """
    for seqid, seq in stream_fasta(fafile):
        if verbose:
            print(f"Seqid: {seqid}\nSequence: {seq}", file=sys.stderr)
        find_dna_repeats(seqid, seq, gaplen, minlen, verbose)


def run():
    """
    Command line run for repeat finder
    """

    parser = argparse.ArgumentParser(description='Calculate the repeat sequences in a DNA sequence')
    parser.add_argument('-f', '--fasta', help='fasta file of DNA sequences')
    parser.add_argument('-m', '--minlen', help='minimum repeat length', type=int, default=11)
    parser.add_argument('-g', '--gaplen', help='gap length (default=0)', type=int, default=0)
    parser.add_argument('--version', help='print the version and exit', action="store_true")
    parser.add_argument('-v', '--verbose', help='verbose output', action='store_true')

    args = parser.parse_args()

    if args.version:
        print(__version__)
        sys.exit(0)

    if not args.fasta:
        print("Please specify at least a fasta file", file=sys.stderr)
        sys.exit(2)

    repeats_in_fasta(args.fasta, args.gaplen, args.minlen, args.verbose)
