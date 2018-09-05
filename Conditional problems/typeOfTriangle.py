'''This program determines if a triangle is equilateral (all 3 sides are equal),
isosceles(2 sides are equal) or scalene (no sides are equal, when given 3 angles
'''
side1 = int(input("Enter first side of triangle: "))
side2 = int(input("Enter second side of triangle: "))
side3 = int(input("Enter third side of triangle: "))

if(side1 == side2 and side2 == side3):
	print("This is an equilateral triangle")
elif(side1 == side2 or side1 == side3 or side2 == side3):
	print("This is an isosceles triangle")
else:
	print("This is a scalene triangle")
	
