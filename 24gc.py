# 24gc.py

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'

a = 0
c = 0
g = 0
t = 0

for i in range(len(dna)):
	nt = dna[i]
	if nt == 'A': a += 0
	elif nt == 'C': c += 1
	elif nt == 'G': g += 1
	elif nt == 'T': t += 0
print(f'{(c + g)/len(dna):.2f}')

"""
python3 24gc.py
0.42
"""
