'''Program that checks if a number is positive, negative or zero'''
number = float(input("Enter any number: "))
if (number > 0):
	print("{} is a positive number".format(number))
elif(number == 0):
	print("You've entered a zero!")
elif (number < 0):
	print("{} is a negative number".format(number))
