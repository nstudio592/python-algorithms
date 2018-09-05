def drawHollowRhombus(rows):
	'''Draws a hollow rhombus'''
	for i in range(rows):
		for j in range(i+1):
			print(" ", end="")
		for j in range(rows):
			if(i==0 or i==rows-1 or j==0 or j==rows-1):
				print("*", end="")
			else:
				print(" ", end="")
		print()
		
r = int(input("Enter the number of rows: "))
drawHollowRhombus(r)
