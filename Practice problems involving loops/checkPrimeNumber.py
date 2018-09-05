def isPrime(n):
	listOfPrimes = []
	for i in range(1, n+1):
		if(n % i == 0):
			listOfPrimes.append(i)
	if(len(listOfPrimes) == 2):
		print(n, "is a prime number")
	else:
		print(n, "is a composite number")

num = int(input("Enter a number to see if it is a prime or composite number: "))
isPrime(num)
