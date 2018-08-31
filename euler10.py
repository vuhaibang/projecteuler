#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.


import time
from math import sqrt


start = time.time()

def isprime(x):
	for i in range(2, int(sqrt(x)) + 1):
		if x % i == 0:
			return False
	return True

## list prime < sqrt(2000000)
prime_list = [2]
for n in range(3, 1500, 2):
	if (isprime(n)):
		prime_list.append(n)
sum = sum(x for x in prime_list)
for n in range(1501, 2 * 10 ** 6, 2):
	for p in prime_list:
		if n % p == 0:
			prime = 0
			break
		prime = n
	sum += prime

print(sum)
print(time.time() - start)
