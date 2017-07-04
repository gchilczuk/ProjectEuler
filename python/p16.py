import time
# https://projecteuler.net/problem=16
start = time.time()
# brute force
number = 2**1000
sum_of_digits = 0
while number > 0:
	sum_of_digits += number % 10
	number //=10

print('result is', sum_of_digits)
print("evaluated in: ", time.time() - start,'s')