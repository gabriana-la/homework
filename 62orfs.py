# 62orfs.py

# Make a program that finds open reading frames in the E. coli genome
# Your program should read a fasta file
# There should be an optional minimum ORF size with a default value of 300 nt
# The output should be a table showing 4 columns
#     1. parent sequence identifier
#     2. begin coordinate
#     3. end coordinate
#     4. strand
#     5. first 10 amino acids of the protein

# Hint: use argparse, mcb185.read_fasta(), and mcb185.translate()
# Hint: don't use the whole genome for testing

# Note: your genes should be similar to those in the real genome

import argparse
import mcb185
import re

parser = argparse.ArgumentParser(description='ORF finder')
parser.add_argument('file', type=str, metavar='<path>', help='fasta file')
parser.add_argument('-n', required=False, type=int, default=300,
	metavar='<int>', help='default minimum ORF size [%(default)i]')
arg = parser.parse_args()

for name, seq in mcb185.read_fasta(arg.file):
	for f in range(3):
		aaseq = mcb185.translate(seq, frame=f)
		orf = 'M\w+\*'
		for match in re.finditer(orf, aaseq):
			protein = match.group()
			if len(protein)*3 >= arg.n:
				print(name[0:11], 3*match.start()+1+f, 3*match.end()+f, '+', protein[0:10])

for name, seq in mcb185.read_fasta(arg.file):
	antidna = mcb185.anti(seq)
	for f in range(3):
		antiaaseq = mcb185.translate(antidna, frame=f)
		orf = 'M\w+\*'
		for match in re.finditer(orf, antiaaseq):
			protein = match.group()
			if len(protein)*3 >= arg.n:
				print(name[0:11], len(seq)-(3*match.end()-1+f), len(seq)-(3*match.start()+f), '-', protein[0:10])

"""
python3 62orfs.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz
NC_000913.3 108 500 - MVFSIIATRW
NC_000913.3 337 2799 + MRVLKFGGTS
NC_000913.3 2801 3733 + MVKVYAPASS
NC_000913.3 3512 4162 - MSHCRSGITG
NC_000913.3 3734 5020 + MKLYNLKDHN
NC_000913.3 3811 4119 - MVTGLSPAIW
NC_000913.3 5310 5738 - MKIPPAMANW
NC_000913.3 5683 6459 - MLILISPAKT
NC_000913.3 6529 7959 - MPDFFSFINS
NC_000913.3 7366 7773 + MKTASDCQQS
"""
