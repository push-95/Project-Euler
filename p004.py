# Problem 4 - Largest Palindrome Product
# Pushyami Shandilya
# http://github.com/push-95

def calc_largest_palindrome():
	'''
	Function to find the largest palindrome made from the product of two 3-digit numbers.
	'''
	return max(i*j for i in range(999,100,-1) for j in range(999,100,-1) if str(i*j)==str(i*j)[::-1])

if __name__ == '__main__':
	print calc_largest_palindrome()