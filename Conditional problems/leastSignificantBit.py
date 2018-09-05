'''This program determines if the least significant
bit (last bit) of a number is 1 or 0 in binary'''
number = int(input("Enter any number: "))

if (number & 1 == 1):
	'''The program checks to see if the number's binary value AND 
	1 evaluate to 1 in boolean algebra'''
	print("Least significant bit of {} is set to 1".format(number))
else:
	print("Least significant bit of {} is set to 0".format(number))
	
