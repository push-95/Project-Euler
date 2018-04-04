# Problem 1 - Multiples of 3 and 5
# Pushyami Shandilya
# http://github.com/push-95

def calc_sum(N):
	'''
	Function to find the sum of all the multiples of 3 or 5 below a number N.
	'''
	return sum(i for i in range(N) if (i%3==0 or i%5==0))

if __name__ == '__main__':
	print calc_sum(1000)