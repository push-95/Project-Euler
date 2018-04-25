# Problem 6 - Square of sum minus sum of squares
# Pushyami Shandilya
# http://githb.com/push-95

def diff(N):
	'''
	Function to find the difference between the square of sum minus sum of squares from 1 to N numbers.
	'''
	sq_of_sum = (sum(i for i in range(1, N + 1)))**2
	sum_of_sq = sum(i**2 for i in range(1, N + 1))
	return str(sq_of_sum - sum_of_sq)


if __name__ == "__main__":
	print(diff(100))