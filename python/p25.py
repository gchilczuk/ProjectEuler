import time
# https://projecteuler.net/problem=25

def Fibonacci_generator():
	a = 0
	b = 1
	while True:
		a, b = b, a+b
		yield a

if __name__ == '__main__':
	start = time.time()
	fib_gen = Fibonacci_generator()
	fib_number = next(fib_gen)
	index = 1
	while len(str(fib_number)) < 1000:
		fib_number = next(fib_gen)
		index += 1

	print("index of the first Fibonacci number with 1000 digits is", index)
	print("Evaluated in: {} seconds".format(time.time() - start))

