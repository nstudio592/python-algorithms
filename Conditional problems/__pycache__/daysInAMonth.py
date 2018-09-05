def isLeapYear(year):
	'''This function determines if a year is a leap year or not.
	This is to ensure the number of days in february is accurate'''
	if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
		return True
	else:
		return False

month = input("Enter month: ")
if(month.lower() == "september" or month.lower()=="april" or month.lower()=="june" or month.lower()=="november"):
	print(month, "has 30 days")
elif(month.lower() == "february"):
	y = int(input("Enter year: "))
	if (isLeapYear(y)):
		print ("February has 29 days since its a leap year.")
	else:
		print("February has 28 days since it isnt a leap year.")
elif(month.lower() == "january" or month.lower()=="march" or month.lower()=="may" or month.lower()=="july"
	or month.lower()=="august" or month.lower()=="october" or month.lower()=="december"):
	print(month, "has 31 days.")
