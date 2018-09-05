def factorial(n):
	'''Function to calculate factorial i.e the product of a number
	and all positive whole numbers below it'''
	for i in range(1, n):
		n = n*i 
	return n

num = int(input("Enter positive number to find its factorial: "))
print("{} factorial = {}".format(num, factorial(num)))
