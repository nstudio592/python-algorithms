def drawSquare(n):
	'''Draw a square made of characters'''
	for i in range(n):
		for j in range(n):
			print("* ", end="")
		print()

rows = int(input("Enter number of rows in the square: "))
drawSquare(rows)
