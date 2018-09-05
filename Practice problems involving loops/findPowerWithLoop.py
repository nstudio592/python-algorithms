def power(x, y):
	'''Use a loop to raise a number to a power inputted by the user'''
	for i in range(y-1):
		x = x*x
	return x

num = int(input("Enter number to raise it to a power: "))
exp = int(input("Enter power: "))

print("{} to the power {} = {}".format(num, exp, power(num, exp)))
