[![Edwards Lab](https://img.shields.io/badge/Bioinformatics-EdwardsLab-03A9F4)](https://edwards.sdsu.edu/research)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![GitHub language count](https://img.shields.io/github/languages/count/linsalrob/repeat_finder)
[![DOI](https://www.zenodo.org/badge/671497428.svg)](https://www.zenodo.org/badge/latestdoi/671497428)

# Repeat Finder - Finding Repeats in DNA sequences

Repeatfinder is a stand alone program to quickly find repeats in DNA sequences. You might find that it is remarkably similar to an essential module in [PhiSpy](http://github.com/linsalrob/PhiSpy).

# How to find repeats


## Using the command line
You can use the `pydna_repeatfinder` command to find repeats in a fasta sequence.

By default, `pydna_repeatfinder` just prints the repeats in a `simple` tab-separated format that is easy to read and includes the DNA sequence.

For example:

```
$ pydna_repeatfinder -f tests/test_long.fasta
random_sequence Number:1        Len1:52 Len2:52 92      144     1946    1998    TCAGTTGTCGTAGGTTAGCCTAAGGGTATCGCGGAAGTATGGAGTATACGGT    TCAGTTGTCGTAGGTTAGCCTAAGGGTATCGCGGAAGTATGGAGTATACGGT
random_sequence Number:2        Len1:52 Len2:52 92      144     197     145     TCAGTTGTCGTAGGTTAGCCTAAGGGTATCGCGGAAGTATGGAGTATACGGT    CACCGTATACTCCATACTTCCGCGATACCCTTAGGCTAACCTACGACAACTG
random_sequence Number:3        Len1:53 Len2:53 145     198     1998    1945    CACCGTATACTCCATACTTCCGCGATACCCTTAGGCTAACCTACGACAACTGA   ATCAGTTGTCGTAGGTTAGCCTAAGGGTATCGCGGAAGTATGGAGTATACGGT
```

There are two long repeats here. The first from 92-144 is repeated in the same orientation (a direct repeat) at position 1946-1998.

We can also output the results formated so you can paste them directly into a GenBank file. This is perhaps the easiest way to visualise the repeats.

```
$ pydna_repeatfinder -f tests/test_long.fasta -o genbank
     repeat_region   join(92..144,1946..1998)
                     /note="direct repeat number 1 of length 53"
                     /rpt_type="direct"
     repeat_region   join(92..144,complement(197..145))
                     /note="inverted repeat number 2 of length 53"
                     /rpt_type="inverted"
     repeat_region   join(145..198,complement(1998..1945))
                     /note="inverted repeat number 3 of length 54"
                     /rpt_type="inverted"
```

## In your own code

You can import the `pydna_repeatfinder` module and use it in your own code:


```
from PyRepeatFinder import find_repeats

r = find_repeats(dna_seq, gap_len, min_len, 0)
for rpt in r:
	# rpt is a dictionary with keys:
	# repeat_number
	# first_start
	# first_end
	# second_start
	# second_end
```

We are happy to add more output formats, please post a GitHub issue and tag it as an enhancement.

# Installing pydna_repeatfinder

You should install it using [bioconda](https://bioconda.github.io/):

```
mamba create -n pydna_repeatfinder -c bioconda pydna_repeatfinder
mamba activate pydna_repeatfinder
```

# Citing pydna_repeatfinder

Please see the citation file.



