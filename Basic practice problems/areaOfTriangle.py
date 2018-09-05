def areaOfTriangle(base,height):
	'''This function calculates the area of a triangle
	when the base and height are inputted'''
	area = 0.5*(base*height)
	return area

x = float(input("Enter length of the triangle's base: "))
y = float(input("Enter length of the traingle's height: "))
print("Area of the triangle = {:.2f}".format(areaOfTriangle(x,y)))
