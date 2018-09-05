def raisePower(x, y):
	'''This function raises any integer to any power ex: 5^2 would be 25
	'''
	return x**y

num = int(input("Enter an integer: "))
n = int(input("Enter the power you'd like to raise the number by: "))
print("{} raised to the power {} is: {}".format(num, n, raisePower(num, n)))
