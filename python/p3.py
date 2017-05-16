import time

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

#  solution:
a = 600851475143
b = a // 2 + 1

for i in range (2,b):
	odwrotna_reszta = a % i
	if odwrotna_reszta == 0:
		dzielnik = a / i
		a /= i
		tf = is_prime(dzielnik)
		if tf:
			print (dzielnik)
			break

print('czas:', time.time() - start)


start = time.time()

def getMaxPrime(n):
    while True:
        for x in range(2, int(n)):
            if n % x == 0:
                n /= x
                getMaxPrime(n)
                break
        else:
            return int(n)

print("Answer:", getMaxPrime(600851475143), "Elapsed:", time.time() - start)


# c = 0
# tf = False
# if b % 2 == 0:
# 	b -= 1
# counter = 0
# for x in range(b, 2, -2):
# 	reszta = a % x
# 	if reszta == 0:
# 		tf = is_prime(x)
# 		print(x, 'dzieli bez reszty')
# 	else:
# 		if counter >= 1000001:
# 			print( 'NOT', x, 'reszta: ', reszta)
# 			counter = 0
# 	if tf:
# 		c = x
# 		break
# 	counter += 1

# print (c)