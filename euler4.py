#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.



def ispalin(x):
	if str(x) == str(x)[:: -1]:
		return True


result = 0
for a in range(999, 800, -1):
	for b in range(999, 800, -1):
		c = a * b
		if (ispalin(c)):
			result = max(result, c)
print(result)