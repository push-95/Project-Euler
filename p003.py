# Problem 1 - Largest Prime factor
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

	
# def primes(n):
	# if n<=2:
#        return []
#    sieve=[True]*(n+1)
#    for x in range(3,int(n**0.5)+1,2):
#        for y in range(3,(n//x)+1,2):
#            sieve[(x*y)]=False

#    return [2]+[i for i in range(3,n,2) if sieve[i]]



# def find_prime_facs(n):
#   list_of_factors=[]
#   i=2
#   while n>1:
#     if n%i==0:
#       list_of_factors.append(i)
#       n=n/i
#       i=i-1
#     i+=1  
#   return list_of_factors



if __name__ == '__main__':
	print calc_largest_prime(600851475143)