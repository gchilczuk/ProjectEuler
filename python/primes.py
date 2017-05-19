import time
# generating primes
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

def remove_mult(num, tab):
	newtab = []
	for i in tab:
		if i % num != 0:
			newtab += [i]
	return newtab


#  brute force solution:
primes = [2]

for i in range(2000001,10000000, 2):
	if is_prime(i):
		primes += [i]

# nums = list(range(2,2000000))
# howmany = 0
# lastmany = time.time()
# wsumie = 0

# while len(nums)>0:
# 	primes += [nums[0]]
# 	nums = remove_mult(nums[0], nums)
# 	howmany += 1
# 	if howmany >= 100:
# 		wsumie += howmany
# 		print(wsumie,'ostatnio w', time.time() - lastmany, 's,  największa to', primes[-1])
# 		lastmany = time.time()
# 		howmany = 0

print("evaluated in: ", time.time() - start,'s')
f = open('primes', 'a')
for i in primes:
	f.write(str(i)+'\n')
f.close()


print("po zapisie: ", time.time() - start,'s')