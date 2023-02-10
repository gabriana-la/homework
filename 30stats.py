# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys

import sys

# print(sys.argv)

vals = []
for thing in sys.argv[1:]:
	vals.append(float(thing))
# print(vals)

print('Count:', len(vals))

print('Minimum:', min(vals))

print('Maximum:', max(vals))

mean = sum(vals)/len(vals)
print('Mean:', f'{mean:.3f}')

sum = 0
for val in vals:
	sum += (val - mean) ** 2
variance = sum / len(vals)
std_dev = variance ** 0.5
	
print('Std. dev:', f'{std_dev:.3f}')

vals.sort()
mid = len(vals) // 2
median = None

if len(vals) % 2 == 0:
	median = (vals[mid] + vals[mid - 1]) / 2
else: 
	median = vals[mid]
print('Median:', f'{median:.3f}')

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
