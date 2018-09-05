def drawHollowSquare(rows, columns):
	'''Draws a hollow square ex:
	****
	*  *
	*  *
	****
	'''
	for i in range(rows):
		for j in range(columns):
			if(i==0 or i==rows-1 or j==0 or j==columns-1):
				print("*", end="")
			else:
				print(" ", end="")
		print()

r = int(input("Enter number of rows in the square: "))
c = int(input("Enter number of columns in the square: "))
drawHollowSquare(r,c)
