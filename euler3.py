# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


from math import sqrt


def isprime(x):
	for i in range(2, int(sqrt(x)) + 1):
		if x % i == 0:
			return False
	return True


for i in range(775147, 1, -2):
	if 600851475143 % i == 0 and (isprime(i)):
		print(i)
		break
