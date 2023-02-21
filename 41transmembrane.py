# 41transmembrane.py

# Write a program that predicts which proteins in a proteome are transmembrane

# Transmembrane proteins are characterized by having
#    1. a hydrophobic signal peptide near the N-terminus
#    2. other hydrophobic regions to cross the plasma membrane

# Both the signal peptide and the transmembrane domains are alpha-helices
# Therefore, they do not contain Proline

# Hydrophobicity can be measured by Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot

# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

# Hint: copy mcb185.py to your homework repo and import that
# Hint: create a function for KD calculation
# Hint: create a function for hydrophobic alpha-helix
# Hint: use the same function for both signal peptide and transmembrane


import sys
import mcb185

"""
# list format
def hydropathy(seq):
	total = 0
	aas = [A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y]
	kd = [1.8, ...]
	
	for aa in seq:
		idx = aas.find[aa]
		total += kd[idx]
"""
# long way
def kd(seq):
	h = 0 # hydrophobicity 
	for aa in seq:
		if   aa == 'A': h +=  1.8
		elif aa == 'C': h +=  2.5
		elif aa == 'D': h += -3.5
		elif aa == 'E': h += -3.5
		elif aa == 'F': h +=  2.8
		elif aa == 'G': h += -0.4
		elif aa == 'H': h += -3.2
		elif aa == 'I': h +=  4.5
		elif aa == 'K': h += -3.9
		elif aa == 'L': h +=  3.8
		elif aa == 'M': h +=  1.9
		elif aa == 'N': h += -3.5
		elif aa == 'P': h += -1.6
		elif aa == 'Q': h += -3.5
		elif aa == 'R': h += -4.5
		elif aa == 'S': h += -0.8
		elif aa == 'T': h += -0.7
		elif aa == 'V': h +=  4.2
		elif aa == 'W': h += -0.9
		elif aa == 'Y': h += -1.3
	return h/len(seq)
	
# hah = hydrophobic alpha helix	
def hah(seq, w, t):	# w = window size/number of aa, t = kd value	
	for i in range(len(seq) - w + 1):
		win = seq[i: i + w]
		if 'P' not in win and kd(win) >= t: return True
	return False

# signal peptides: 8 aa, kd > 2.5, first 30 aa
# transmembrane alpha helix: 11 aa, kd > 2.0, after first 30 aa

for name, seq in mcb185.read_fasta(sys.argv[1]):
	nterm = seq[0:30]
	cterm = seq[30:]
	if hah(nterm, 8, 2.0) and hah(cterm, 11, 2.5):
		print(name)

"""
python3 41transmembrane.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
NP_414560.1 Na(+):H(+) antiporter NhaA [Escherichia coli str. K-12 substr. MG1655]
NP_414568.1 lipoprotein signal peptidase [Escherichia coli str. K-12 substr. MG1655]
NP_414582.1 L-carnitine:gamma-butyrobetaine antiporter [Escherichia coli str. K-12 substr. MG1655]
NP_414607.1 DedA family protein YabI [Escherichia coli str. K-12 substr. MG1655]
NP_414609.1 thiamine ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414653.1 protein AmpE [Escherichia coli str. K-12 substr. MG1655]
NP_414666.1 quinoprotein glucose dehydrogenase [Escherichia coli str. K-12 substr. MG1655]
NP_414695.1 iron(III) hydroxamate ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414699.1 PF03458 family protein YadS [Escherichia coli str. K-12 substr. MG1655]
NP_414717.2 CDP-diglyceride synthetase [Escherichia coli str. K-12 substr. MG1655]
...
"""
