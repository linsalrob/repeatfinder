"""
Command line invocations for find_repeats
"""

import sys
import argparse
from PyRepeatFinder import find_repeats
from .sequences import stream_fasta
from .repeat_search import RepeatSearch
from ._version import __version__

__author__ = 'Rob Edwards'

def simple_print(seqid, dna_seq, repeats):
    """
    Print the repeats in a simple, text based format
    """
    ## NOTE: The numbers returned by find_repeats are 1 indexed!!
    for rpt in repeats:
        if rpt['first_end'] > rpt['first_start']:
            start1 = rpt['first_start'] - 1
            rptlen1 = rpt['first_end'] - rpt['first_start']
        else:
            start1 = rpt['first_end'] - 1
            rptlen1 = rpt['first_start'] - rpt['first_end']

        if rpt['second_end'] > rpt['second_start']:
            start2 = rpt['second_start'] - 1
            rptlen2 = rpt['second_end'] - rpt['second_start']
        else:
            start2 = rpt['second_end'] - 1
            rptlen2 = rpt['second_start'] - rpt['second_end']

        seq1 = dna_seq[start1:start1 + rptlen1]
        seq2 = dna_seq[start2:start2 + rptlen2]
        data = [seqid, f"Number:{rpt['repeat_number']}", f"Len1:{rptlen1}",
                f"Len2:{rptlen2}",
                rpt['first_start'], rpt['first_end'],
                rpt['second_start'], rpt['second_end'],
                seq1, seq2
                ]
        print("\t".join(map(str, data)))

def genbank_print(repeats):
    """
    Print the repeats in genbank format
    """

    rpt_type =None
    for rpt in repeats:
        if rpt['first_end'] > rpt['first_start']:
            loc1 = f"{rpt['first_start']}..{rpt['first_end']}"
            rpt_len = rpt['first_end'] - rpt['first_start'] + 1
            if rpt['second_end'] > rpt['second_start']:
                rpt_type = 'direct'
                loc2 = f"{rpt['second_start']}..{rpt['second_end']}"
            else:
                rpt_type = 'inverted'
                loc2 = f"complement({rpt['second_start']}..{rpt['second_end']})"
        else:
            loc1 = f"complement({rpt['first_start']}..{rpt['first_end']})"
            rpt_len = rpt['first_start'] - rpt['first_end'] + 1
            if rpt['second_end'] < rpt['second_start']:
                rpt_type = 'direct'
                loc2 = f"complement({rpt['second_start']}..{rpt['second_end']})"
            else:
                rpt_type = 'inverted'
                loc2 = f"{rpt['second_start']}..{rpt['second_end']}"

        print(f"     repeat_region   join({loc1},{loc2})")
        print(f"                     /note=\"{rpt_type} repeat number {rpt['repeat_number']} of length {rpt_len}\"")
        print(f"                     /rpt_type=\"{rpt_type}\"")


def find_dna_repeats(rpt_search, verbose=False):
    """
    find the repeats in a dna sequence
    """

    if verbose:
        print(f"Finding repeats in {rpt_search.seqid} with seq {rpt_search.dnaseq}", file=sys.stderr)

    r = find_repeats(rpt_search.dnaseq, rpt_search.gaplen, rpt_search.minlen, 0)

    ## NOTE: The numbers returned by find_repeats are 1 indexed!!
    if rpt_search.output == 'simple':
        simple_print(rpt_search.seqid, rpt_search.dnaseq, r)
    elif rpt_search.output == 'genbank':
        genbank_print(r)



def repeats_in_fasta(rpt_search, verbose=False):
    """
    Find all the repeats in the sequences in a fasta file
    """
    for seqid, seq in stream_fasta(rpt_search.fastafile):
        if verbose:
            print(f"Seqid: {seqid}\nSequence: {seq}", file=sys.stderr)
        rpt_search.dnaseq = seq
        rpt_search.seqid = seqid
        find_dna_repeats(rpt_search, verbose)


def run():
    """
    Command line run for repeat finder
    """

    output_choices = ['simple', 'genbank']
    parser = argparse.ArgumentParser(description='Calculate the repeat sequences in a DNA sequence')
    parser.add_argument('-f', '--fasta', help='fasta file of DNA sequences')
    parser.add_argument('-m', '--minlen', help='minimum repeat length', type=int, default=11)
    parser.add_argument('-g', '--gaplen', help='gap length (default=0)', type=int, default=0)
    parser.add_argument('-o', '--output', choices=output_choices, help='output format', default='simple')
    parser.add_argument('--version', help='print the version and exit', action="store_true")
    parser.add_argument('-v', '--verbose', help='verbose output', action='store_true')

    args = parser.parse_args()

    if args.version:
        print(__version__)
        sys.exit(0)

    if not args.fasta:
        print("Please specify at least a fasta file", file=sys.stderr)
        sys.exit(2)

    rpt_search = RepeatSearch(args.fasta, args.minlen, args.gaplen,
                              args.output)
    repeats_in_fasta(rpt_search, args.verbose)
