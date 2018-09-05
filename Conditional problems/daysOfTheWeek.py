def daysOfWeek(day):
	'''This function accepts a number from 1 to 7
	and outputs the day associated with that number
	ex: entering 1 will print out Monday, the first day of the 
	week'''
	if(day == "1"):
		return "Monday"
	elif(day == "2"):
		return "Tuesday"
	elif(day == "3"):
		return "Wednesday"
	elif(day == "4"):
		return "Thursday"
	elif(day == "5"):
		return "Friday"
	elif(day== "6"):
		return "Saturday"
	elif(day== "7"):
		return "Sunday"
	else:
		return "Error, number needs to be between 1 to 7"

d = input("Enter number from 1 to 7: ")
print(daysOfWeek(d))
