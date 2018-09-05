def drawRhombus(n):
	'''Draws a rhombus leaning to the left of the screen'''
	for i in range(n):
		for j in range(i+1):
			print(" ", end="")
		for k in range(n):
			print("*", end="")
		print()

rows = int(input("Enter the number of rows in the rhombus: "))
drawRhombus(rows)
