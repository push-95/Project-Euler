# Problem 3 - Largest Prime factor
# Pushyami Shandilya
# http://github.com/push-95

def calc_largest_prime(N):
	'''
	Function to find the largest prime factor of a number N.
	'''
	factors = []

	i = 2
	while N>1:
		if N%i==0:
			factors.append(i)
			N = N/i
			i -= 1
		i += 1
	return factors[-1]

if __name__ == '__main__':
	print calc_largest_prime(600851475143)