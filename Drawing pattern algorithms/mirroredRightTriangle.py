def drawTriangle(n):
	'''draws a mirrored right triangle. Ex:
        *
       **
      ***
	 ****
	*****
	'''
	for i in range(n):
		for j in range(n-i):
			print(" ", end="")
		for k in range(i+1):
			print("*", end="")
		print()
	
rows = int(input("Enter number of rows in the triangle: "))
drawTriangle(rows)
