#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?


from math import sqrt


def isprime(x):
	for i in range(2, int(sqrt(x)) + 1):
		if x % i == 0:
			return False
	return True


count = 2
number = 3
while  count < 10001:
	number += 2
	if (isprime(number)):
		count += 1
print(number)