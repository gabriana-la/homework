# 25atseq.py

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# Note: set random.seed() if you want repeatable random numbers

# generate random DNA sequence
import random
n = 30
x = .60
dna = ''

for i in range(n):
	r = random.random()
	if r < x: dna += random.choice('AT')
	else: dna += random.choice('CG')

# calculate AT fraction
a = 0
c = 0
g = 0
t = 0
for nt in dna:
	if nt == 'A': a += 1
	elif nt == 'C': c += 0
	elif nt == 'G': g += 0
	else: t += 1
AT_frac = (a + t)/len(dna)

# report length, AT fraction, sequence
print(len(dna), AT_frac, dna)

"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
