# 71gff.py

# Write a program that converts genes in gff into JSON
# Use the minaturized version of the C. elegans genome (included) this time
# Organize the genes onto chromosomes
# Print the number of genes on each chromosome to stderr
# Your code should mimic the output below

# Hint: your outer data structure is a dictionary

# Note: gene names are stored differently here than the last file

import sys
import gzip
import re
import json

filename = sys.argv[1]

chromosomes = {}
genome = {}

with gzip.open(filename, 'rt') as fp:
	for line in fp:
		for match in re.finditer('\s+gene\s+', line):
			f = line.split()
			chromosome = f[0]
			if chromosome not in chromosomes: chromosomes[chromosome] = 0 
			chromosomes[chromosome] +=1
			
			name = re.search('sequence_name=(\w+\.\w+)', line)
			gene = str(name.group(1))
			
			coordinates = re.search('\s+(\d+)\s+(\d+)\s+', line)
			beg = int(coordinates.group(1))
			end = int(coordinates.group(2))
			
			sense = re.search('\.\s+(.)\s+\.', line)
			strand = sense.group(1)
			
			info = {}
			info['gene'] = gene
			info['beg'] = beg
			info['end'] = end
			info['strand'] = strand
			
			if chromosome not in genome: genome[chromosome] = []
			else: genome[chromosome].append(info)
			
for chromosome in chromosomes:
	print(chromosome, chromosomes[chromosome])			

print(json.dumps(genome, indent=4))

"""
python3 71gff.py elegans
I 37
II 57
III 37
IV 41
MtDNA 2
V 41
X 45
{
    "I": [
        {
            "gene": "Y74C9A.6",
            "beg": 3747,
            "end": 3909,
            "strand": "-"
        },
        {
            "gene": "Y74C9A.3",
            "beg": 4116,
            "end": 10230,
            "strand": "-"
        },
...
"""
