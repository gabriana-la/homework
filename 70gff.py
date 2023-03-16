# 70gff.py

# Write a program that converts genes in gff into JSON
# Use the E. coli genome gff
# Your code should mimic the output below

import sys
import gzip
import re
import json

filename = sys.argv[1]

genome = []

with gzip.open(filename, 'rt') as fp:
	for line in fp:
		if line.startswith('#'): continue
		for match in re.finditer('RefSeq\s+gene', line):
			info = {}
			name = re.search('Name=(\w+)', line)
			gene = str(name.group(1))
			
			coordinates = re.search('(\d+)\s+(\d+)', line)
			beg = int(coordinates.group(1))
			end = int(coordinates.group(2))
			
			sense = re.search('\.\s+(.)\s+\.', line)
			strand = sense.group(1)
			
			info['gene'] = gene
			info['beg'] = beg
			info['end'] = end
			info['strand'] = strand
			genome.append(info)

print(json.dumps(genome, indent=4))


"""
python3 70gff.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.gff.gz
[
    {
        "gene": "thrL",
        "beg": 190,
        "end": 255,
        "strand": "+"
    },
    {
        "gene": "thrA",
        "beg": 337,
        "end": 2799,
        "strand": "+"
    },
...
"""
