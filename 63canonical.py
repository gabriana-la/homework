# 63canonical.py

# You probably learned that ATG is the only start codon, but is it?
# Write a program that reports the start codons from the E. coli genome
# Your program must:
#    1. read GCF_000005845.2_ASM584v2_genomic.gbff.gz at the only input
#    2. use a regex to find CDS coordinates
#    3. count how many different start codons there are

# Note: the sequence is at the end of the file
# Note: genes on the negative strand are marked complement(a..b)

# Hint: you can read a file twice, first to get the DNA, then the CDS
# Hint: check your CDS by examining the source protein

import sys
import gzip
import mcb185
import re

filename = sys.argv[1]

# grabbing the sequence
seq = ''

with gzip.open(filename, 'rt') as fp:
	for line in fp:
		if line.startswith('ORIGIN'):
			break
	for line in fp.readlines():
		f = line.split()
		seq += ''.join(f[1:])
seq = seq.upper()

# finding the coordinates
startcs = {}
with gzip.open(filename, 'rt') as fp:
	for line in fp.readlines():
		if line.startswith('     CDS'):
			coordinates = re.search('(\d+)\.\.(\d+)', line)
			beg = int(coordinates.group(1))
			end = int(coordinates.group(2))
			if 'complement' in line:
				startc = mcb185.anti(seq[end - 3: end])
			else:
				startc = seq[beg - 1: beg + 2]
			if startc not in startcs:
				startcs[startc] = 0
			startcs[startc] += 1

for startc in startcs:
	print(startc, startcs[startc])

"""
python3 63canonical.py ~/DATAq/E.coli/GCF_000005845.2_ASM584v2_genomic.gbff.gz
ATG 3883
GTG 338
TTG 80
ATT 5
AGT 1
AAA 1
AGC 1
TTC 1
TAA 1
CGT 1
CTG 2
GAC 1
"""
