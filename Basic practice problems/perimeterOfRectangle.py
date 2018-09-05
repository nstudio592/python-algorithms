def perimeter(width, height):
	'''Function to return perimeter of rectangle given width and height'''
	return 2*(width + height)
	
w = float(input("Enter width of rectange: "))
h = float(input("Enter height of rectangle: "))
print ("The perimeter of the rectangle is: ", perimeter(w, h))
