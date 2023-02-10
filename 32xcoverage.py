# 32xcoverage.py

# Write a program that simulates a shotgun resequencing project
# How uniformly do the reads "pile up" on a chromosome?
# How much of that depends on sequencing depth?

# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line

# Hint: make the problem smaller, so it's easier to visualize and debug
# Hint: if you don't understand the context of the problem, ask for help
# Hint: if you are undersampling the ends, do something about it

# Note: you will not get exactly the same results as the command line below

import random
import sys

genome_size = int(sys.argv[1])

readlen = int(sys.argv[2])

readnum = int(sys.argv[3])

# print(genome_size, readlen, readnum)

genome = [0] * genome_size
# print(genome)

for i in range(readnum):
	start = random.randint(0, len(genome) - readlen)
	# print(start)
	for j in range(readlen):
		genome[j + start] += 1
# print(genome[readlen: -readlen])

print(min(genome[readlen: -readlen]), max(genome[readlen: -readlen]), f'{sum(genome[readlen: -readlen])/(genome_size - 2 * readlen):.5f}')

"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
