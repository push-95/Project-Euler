# Problem 2 - Even Fibonacci numbers
# Pushyami Shandilya
# http://github.com/push-95

def even_fibonacci():
	'''
	Function to find the sum of all even-valued terms in the Fibonacci Series.
	N <= 4,000,000
	'''
	even_list = []
	prev = 1
	curr = 1
	while True:
		prev, curr= curr, prev+curr
		if curr%2==0:
			even_list.append(curr)
		if curr>4000000:
			break

	print sum(even_list)

if __name__ == '__main__':
	print even_fibonacci()