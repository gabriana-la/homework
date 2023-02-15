# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list

import random
import sys

num_days = int(sys.argv[1])

num_people = int(sys.argv[2])
print(num_days, num_people)

trials = 10000
shared = 0


# fill empty calendar, check as you go, fastest but takes up more space
for trial in range(trials):
	calendar = [0] * num_days	
	for i in range(num_people):
		birthday = random.randint(0, num_days - 1)
		if calendar[birthday] == 1:
			shared += 1
			break
		calendar[birthday] += 1
print(shared/trials)


"""
# fill empty calendar, check after, slow
for trial in range(trials):
	calendar = [0] * num_days
	found = False
	for i in range(num_people):
		birthday = random.randint(0, num_days - 1)
		calendar[birthday] += 1
	
	for bday in calendar:
		 if bday > 1:
		 	found = True
		 	break
	if found:
		 shared += 1
print(shared/trials)
"""

"""
# create birthdays, check as you go, 2nd fastest but takes up less space
for trial in range(trials):
	birthdays = []
	for i in range(num_people):
		birthday = random.randint(0, num_days - 1)
		if birthday in birthdays:
			shared += 1
			break
		birthdays.append(birthday)
print(shared/trials)
"""

"""
# create birthdays, compare against each (pairwise comparison), slowest
for trial in range(trials):
	birthdays = []	
	for i in range(num_people):
		birthdays.append(random.randint(0, num_days - 1))
		found = False
		for j in range(i + 1, num_people):
			if birthdays[i] == birthdays[j]:
				found = True
				break
		if found:
			shared += 1
			break
print(shared/trials)
"""

"""
python3 33birthday.py 365 23
0.571
"""

