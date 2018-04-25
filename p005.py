# Problem 5 - Smallest Multiple
# Pushyami Shandilya
# http://github.com/push-95

import fractions

def calc_smallest_multiple(N):
	'''
	Function to find the smallest positive number that is evenly divisible by all of the numbers from 1 to 20.
	'''
	res = 1
	for i in range(1,N+1):
		res *= i//fractions.gcd(res, i)
	return res

if __name__ == "__main__":
	print(calc_smallest_multiple(20))