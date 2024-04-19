"""
Command line invocations for find_repeats
"""

import sys
import argparse
from PyRepeatFinder import find_repeats
from .sequences import stream_fasta

__author__ = 'Rob Edwards'

def find_dna_repeats(seqid, dna_seq, gap_len=0, verbose=False):
    """
    find the repeats in a dna sequence
    """

    if verbose:
        print(f"Finding repeats in {seqid} with seq {dna_seq}", file=sys.stderr)

    r = find_repeats(dna_seq, gap_len)

    for rpt in r:
        rptlen = rpt['first_end']-rpt['first_start']+1
        data = [seqid, f"Number:{rpt['repeat_number']}", f"Len:{rptlen}",
                rpt['first_start'], rpt['first_end'],
                rpt['second_start'], rpt['second_end']
               ]
        print("\t".join(map(str, data)))


def repeats_in_fasta(fafile, gaplen, verbose=False):
    """
    Find all the repeats in the sequences in a fasta file
    """
    for seqid, seq in stream_fasta(fafile):
        if verbose:
            print(f"Seqid: {seqid}\nSequence: {seq}", file=sys.stderr)
        find_dna_repeats(seqid, seq, gaplen, verbose)


def run():
    """
    Command line run for repeat finder
    """

    parser = argparse.ArgumentParser(description='Calculate the repeat sequences in a DNA sequence')
    parser.add_argument('-f', help='fasta file of DNA sequences', required=True)
    parser.add_argument('-g', help='gap length (default=0)', type=int, default=0)
    parser.add_argument('-v', help='verbose output', action='store_true')
    args = parser.parse_args()

    repeats_in_fasta(args.f, args.g, args.v)
