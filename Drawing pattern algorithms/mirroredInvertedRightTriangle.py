def drawTriangle(n):
	'''draws an inverted mirrored right triangle. Example:
	*****
	 ****
	  ***
	   **
	    *
	  '''
	for i in range(n):
		for j in range(i+1):
			print(" ", end="")
		for k in range(n-i):
			print("*", end="")
		print()

rows = int(input("Enter number of rows in the triangle: "))
drawTriangle(rows)

