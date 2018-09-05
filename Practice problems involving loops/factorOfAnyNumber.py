def findFactor(n):
	'''Program to find all factors of a given number'''
	for i in range(1, n+1):
		if(n % i == 0):
			print(i)

num = int(input("Enter any number to find its factors: "))
findFactor(num)
