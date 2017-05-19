import time
# generating primes
start = time.time()
# brute force
f = open('big_numbers', 'r')
summary = 0
for line in f:
	summary += int(line)

print(str(summary)[:10])

print("evaluated in: ", time.time() - start,'s')