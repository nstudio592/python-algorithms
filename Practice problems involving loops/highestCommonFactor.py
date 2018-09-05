def findHCF(x, y):
	'''Find highest common factor between 2 numbers'''
	smallest = min(x, y)
	for i in range(1, smallest + 1):
		if(x % i == 0 and y % i == 0):
			hcf = i
	return hcf

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Highest common factor of {} and {} = {}".format(num1, num2, findHCF(num1, num2)))
	
