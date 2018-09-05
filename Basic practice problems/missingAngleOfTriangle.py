def findThirdAngle(angleA, angleB):
	'''This function calculates the third angle of a triangle
	given two valid angles.'''
	angleC = 180 - (angleA + angleB)
	return angleC

a = int(input("Enter first angle of triangle: "))
b = int(input("Enter second angle of triangle: "))
c = findThirdAngle(a, b)

if (c <= 0):
	print("Error. Based on the size of the angles you've entered, that shape is not a triangle.")
else:
	print("The third angle of the triangle is: {} degrees".format(c))
