def drawTriangle(rows):
	'''Draws an upside down triangle with hypotenuse facing left like:
	*****
	****
	***
	**
	*
	'''
	for i in range(rows):
		for j in range(rows-i):
			print("* ", end="")
		print()

n = int(input("Enter number of rows: "))
drawTriangle(n)
