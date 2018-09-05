def cmToMeters(cm):
	'''This function converts centimeters to meters'''
	return cm / 100

def cmToKilometers(cm):
	'''This function converts centimeters to kilometers'''
	return cm / 100000

length = int(input("Enter length in centimeters: "))
print("Length in Meters : ", cmToMeters(length))
print("Length in Kilometers : ", cmToKilometers(length))
	
