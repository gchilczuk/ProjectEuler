import time
# brute force
start = time.time()

a, b = 0, 0
for i in range(1,101):
	a += i*i
	b += i

print('result:', b*b - a)

print(time.time() - start,'s')