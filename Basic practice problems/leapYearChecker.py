def isLeapYear(year):
	'''This function determines if a year is a leap year or not.'''
	if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
		return "Leap Year"
	else:
		return "Common Year"

y = int(input("Enter a year: "))
print (isLeapYear(y))
