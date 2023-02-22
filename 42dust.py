# 42dust.py

# Write a program that performs entropy filtering on nucleotide fasta files
# Windows that are below the entropy threshold are replaced by N

# Program arguments include file, window size, and entropy threshold

# Output should be a fasta file with sequence wrapped at 60 characters

# Hint: use the mcb185 library
# Hint: make up some fake sequences for testing

# Note: don't worry about "centering" the entropy on the window (yet)

import sys
import mcb185
import math


file = sys.argv[1]
w = int(sys.argv[2]) # w = window size
et = float(sys.argv[3]) # et = entropy threshold


# entropy calculator 
def entropy(probs):
	assert(math.isclose(1.0, sum(probs)))
	h = 0
	for p in probs:
		if p != 0: h -= p * math.log2(p)
	return h

# seq entropy calculator
def seq_entropy(seq):
	A = seq.count('A')/len(seq)
	C = seq.count('C')/len(seq)
	G = seq.count('G')/len(seq)
	T = seq.count('T')/len(seq)
	return entropy([A, C, G, T])

for name, seq in mcb185.read_fasta(sys.argv[1]):
	seq1 = list(seq)
	for i in range(len(seq) - w + 1):
		win = seq[i: i + w]
		ewin = seq_entropy(win)
		if ewin < et: seq1[i] = 'N'
	# if seq_entropy(seq[i: i + w]) < et: # same as the lines above
	seq = ''.join(seq1)
	print(seq)

"""
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in range(len(seq) - w + 1):
		win = seq[i: i + w]
		if entropy(win) = 0: continue
		if entropy(win) < et: print('N')
		print(i, win, entropy(win))
"""	


"""
python3 42dust.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 11 1.4
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGNTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTNNNNNNNAAAAAGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGNNNNNNNNNNNATTTTATTGACTTAGG
TCACNNAATACTTTAACCAATATAGGCATAGCGCACAGNCNNNNAAAAATTACAGAGTNN
ACAACATCCATGAAACGCATTAGCACCACCATNNNNNNNACCATCACCATTACCACAGGT
AACNGTGCGGGCTGACGCGTACAGNNNNNNNNGAAAAAAGCCCGCACCTGACAGTGCNNN
NNNTTTTTTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
ANNCANGGGCAGGTGGCCANCGNNNNNNNTNNNCCCGNNNNNNNNNCCAACCACCTGGTG
GCGATNATTGNNAAAACCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
...
"""
