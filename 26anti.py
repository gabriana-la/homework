# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

dna = 'ACTGAAAAAAAAAAA'
revcomp = ''

for i in range(len(dna)):
	nt = dna[i]
	if   nt == 'A': revcomp = 'T' + revcomp
	elif nt == 'C': revcomp = 'G' + revcomp
	elif nt == 'G': revcomp = 'C' + revcomp
	else:           revcomp = 'A' + revcomp
print(revcomp)

"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""
