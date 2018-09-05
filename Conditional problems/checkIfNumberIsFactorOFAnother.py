'''Program asks user to enter a number. 
Program then asks user for 2 other numbers,
and checks if the are factors of first number entered.'''


n = int(input("Enter any number: "))
firstVal = int(input("Enter first number to see if it is a factor of {}: ".format(n)))
secondVal = int(input("Enter second number to see if it is a factor of {}: ".format(n)))

if(n % firstVal == 0 and n % secondVal == 0):
	print("Both {} and {} are factors of {}".format(firstVal, secondVal, n)) 
elif(n % firstVal == 0):
	print("{} is factor of {} and {} is not".format(firstVal, n, secondVal))
elif(n % secondVal == 0):
	print("{} is factor of {} and {} is not".format(secondVal, n, firstVal))
else:
	print("Neither {} nor {} are factors of {}".format(firstVal, secondVal, n))
