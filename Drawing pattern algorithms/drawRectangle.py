def drawSquare(row, col):
	'''Draw a rectangle made of characters'''
	for i in range(row):
		for j in range(col):
			print("* ", end="")
		print()

rows = int(input("Enter number of rows in the rectangle: "))
cols = int(input("Enter number of columns in the rectangle: "))
drawSquare(rows, cols)


