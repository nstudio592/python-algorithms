def areaOfRectangle(width, height):
	'''Function to return area of rectangle given width and height'''
	return width*height

w = float(input("Enter width of rectangle: "))
h = float(input("Enter height of rectangle: "))
print("Area of the rectangle is: ", areaOfRectangle(w, h))
