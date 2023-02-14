# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list

import random
random.seed(1)
import sys

num_days = int(sys.argv[1])

num_people = int(sys.argv[2])
print(num_days, num_people)


calendar = [0] * num_days
print(calendar)

birthday = random.randint(0, num_days)
print(birthday)
	
for i in calendar:
	if i == birthday:
		calendar[i] += 1
print(calendar)
	

"""
python3 33birthday.py 365 23
0.571
"""

