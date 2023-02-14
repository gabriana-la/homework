# 31entropy.py

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# Store the values in a new list

# Note: make sure the command line values contain numbers
# Note: make sure the probabilities sum to 1.0
# Note: import math and use the math.log2()

# Hint: try breaking your program with erroneous input

import math
import sys

vals = []
for thing in sys.argv[1:]:
	vals.append(float(thing))
# print(vals)

assert(math.isclose(sum(vals), 1.0))

sum = 0
for val in vals:
	sum += (val * math.log2(val))
h = -(sum)
print(f'{h:.3f}')

"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
