# stupid solution:
def multiplies_OFandOF(start, end, of1=3, of2=5):
	li = [x for x in range(start, end) if x % of1 == 0 or x % of2 ==0]
	return sum(li)

print("sum of all the multiples of 3 or 5 below 1000: ", multiplies_OFandOF(1,1000))

# clever solution:
