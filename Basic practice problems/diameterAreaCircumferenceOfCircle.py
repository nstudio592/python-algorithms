'''The following program calculates the diameter, circumference and area
of a circle when given the radius'''
from math import pi

radius = float(input("Enter radius of the circle: "))

diameter = 2*radius
circumference = 2*pi*radius
area = pi * (radius**2)

print("Diameter of circle with radius {} is {}".format(radius, diameter))
print("Circumference of circle with radius {} is {:.2f}".format(radius, circumference))
print("Area of circle with radius {} is {:.2f}".format(radius, area))

