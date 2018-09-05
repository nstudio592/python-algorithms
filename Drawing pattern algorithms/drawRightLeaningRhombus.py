def drawRhombus(n):
	'''Draws a rhombus leaning to the right on the screen'''
	for i in range(n):
		for j in range(n-i):
			print(" ", end="")
		for k in range(n):
			print("*", end="")
		print()

rows = int(input("Enter the number of rows in the rhombus: "))
drawRhombus(rows)
		
