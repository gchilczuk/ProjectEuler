#

def is_palindrome(x):
	x = str(x)
	return x == x[::-1]

def hihhest_3digit_palindrome():
	for i in range(999,900,-1):
		for j in range(999,900,-1):
			pos = i * j
			if is_palindrome(pos):
				return i, j, pos

print(hihhest_3digit_palindrome())