import time
# https://projecteuler.net/problem=10
start = time.time()

def is_prime(x):
	if x == 2:
		return True
	# naive, not so vlever colution
	sqrtx = x ** (1/2)
	sqrtx = int(sqrtx)+1
	for i in range(2, sqrtx):
		if x % i == 0:
			return False
	return True

#  brute force solution:
primes = [2]

for i in range(3,2000000, 2):
	if is_prime(i):
		primes += [i]

print("solution:", sum(primes))
print("evaluated in: ", time.time() - start,'s')