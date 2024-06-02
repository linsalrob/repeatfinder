"""
Initialisation code
"""

from .cli import find_dna_repeats, repeats_in_fasta, run
from .colours import Colours, message
from .rob_error import FastqFormatError, ColorNotFoundError
from .sequences import stream_fastq, stream_fasta, stream_gfa_sequences
from ._version import __version__

__all__ = [
    'find_dna_repeats', 'repeats_in_fasta', 'run',
    'Colours', 'message',
    'FastqFormatError', 'ColorNotFoundError',
    'stream_fastq', 'stream_fasta', 'stream_gfa_sequences',
    '__version__'
]
