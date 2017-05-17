import time
# 10 001st prime
start = time.time()

def is_dividable_by_list(number, dividers):
	for div in dividers:
		if number % div == 0:
			return True
	return False

def infinite_primes_generator():
	primes = [2,3,5]
	for i in primes:
		yield i
	curr_num = 7
	while True:
		if not is_dividable_by_list(curr_num, primes):
			primes += [curr_num]
			yield curr_num
		curr_num += 2

x = 1
for i in infinite_primes_generator():
	# print (i)
	if x == 10001:
		print (i)
		break
	x += 1



print(time.time() - start,'s')