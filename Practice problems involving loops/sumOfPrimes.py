def isPrime(n):
	'''Return a list of prime numbers from 1 to n where n is a value 
	entered by the user'''
	listOfPrimes = []
	for i in range(1, n+1):
		if(n % i == 0):
			listOfPrimes.append(i)
	if(len(listOfPrimes) == 2):
		return True
	else:
		return False

#sum = 0
num = int(input("Enter any positive integer to see sum of primes from 1 to the value you entered (inclusive): "))

for i in range(1, num+1):
	if(isPrime(i)):
		#sum += i
		print(i)

#print(sum)
