def drawTriangle(rows):
	'''Draws a right angle triangle with hypotenuse pointing right like:
	*
	**
	***
	****
	*****'''
	for i in range(rows):
		for j in range(i+1):
			print("* ", end="")
		print()


r = int(input("Enter number of rows in the triangle: "))
print(drawTriangle(r))

