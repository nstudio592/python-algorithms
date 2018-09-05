'''Determines if a shape is a triangle or not when given 3 angles'''
angle1= int(input("Enter first angle of triangle: "))
angle2 = int(input("Enter second angle of triangle: "))
angle3 = int(input("Enter third angle of triangle: "))

total = angle1 + angle2 + angle3

if(total == 180):
	print("Sum of angles is 180 degrees, therefore this is a valid triangle")
else:
	print("Sum of angles is not 180 degrees, therefore this is not a valid triangle")
