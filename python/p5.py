import time

# brute force

start = time.time()
divs = [20, 19, 18, 17, 16, 15, 14, 13, 11]

def is_dividible_by_all(number, divs):
	for i in divs:
		if number % i != 0:
			return False
	return True

number = 2520
while True:
	if is_dividible_by_all(number, divs):
		print ('brute force solution:',number)
		break

	number += 1

print('brute force:',time.time() - start,'s')
# multiplication


start = time.time()

primes = [2,3,5,7,11,13,17,19]

def smallest_prime_div(x):
	for i in primes:
		if x % i == 0:
			return i

number = 1
for i in range(2, 21):
	if number % i != 0:
		number *= smallest_prime_div(i)

print ('minde force solution:',number)

print('mind force:', time.time() - start,'s')
