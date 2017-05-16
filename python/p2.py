# just solution:
def fibonacii_generator(end=4000000):
	a = 1
	b = 1
	while a < end:
		a, b = b, a+b
		yield a

even_fibonacii = [x for x in fibonacii_generator() if x % 2 == 0]
print("sum of the even-valued fibonacci numbers: ", sum(even_fibonacii))

