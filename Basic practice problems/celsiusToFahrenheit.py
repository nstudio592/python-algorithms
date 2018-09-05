def tempConversion(celsius):
	'''Takes a temperature in celsius and converts it to fahrenheit'''
	fahrenheit = (celsius * 9/5) + 32
	return fahrenheit

temp = int(input("Enter temperature in degrees Celsius: "))
print ("{} degrees celsius is {} degrees farenheit".format(temp, tempConversion(temp)))
