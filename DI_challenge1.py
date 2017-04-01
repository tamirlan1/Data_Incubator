from itertools import product
import itertools
import random
import numpy as np
counter = 1
for x1, x2, x3, x4, x5, x6, x7, x8 in itertools.product(range(1, 7), repeat=8):
	M = x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8
	if M == 24:
		# print counter, '---', x1, x2, x3, x4, x5, x6, x7, x8
		counter += 1
print counter
# N = 50
# M_target = 150

# counter = 0
# valid_prods = []
# valid_numbers = []
# while True:
# 	M = 0
# 	P = 1
# 	numbers = []
# 	for i in xrange(N):
# 		x = random.randint(1, 6)
# 		numbers.append(x)
# 		P *= x

# 	if np.sum(numbers) == M_target:
# 		valid_prods.append(P)
# 		valid_numbers = numbers


# 	counter += 1
# 	if counter%1000000 == 0:
# 		print 'Counter:', counter
# 		print 'Number of Valid Entries', len(valid_prods)
# 		print 'Last Entry:',valid_prods[-1]
# 		print 'Numbers:', valid_numbers
# 		print 'Mean:', np.mean(valid_prods)
# 		print 'SD:', np.std(valid_prods)
# 		print ''
# 	# print numbers
			



