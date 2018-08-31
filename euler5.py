# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?



from math import sqrt


def isprime(x):
	for i in range(2, int(sqrt(x)) + 1):
		if x % i == 0:
			return False
	return True	


result = 1
for number in range(2, 21):
	if (isprime(number)):
		number_fix = 1
		while number_fix * number < 20:
			number_fix = number_fix * number
		result *= number_fix
print(result)