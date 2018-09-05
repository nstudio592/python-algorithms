def drawPyramid(n):
	'''draws an upside down pyramid'''
	for i in range(n):
		for j in range(i+1):
			print(" ", end="")
		for k in range((2*n)-(2*i+1)):
			print("*", end="")
		print()

rows = int(input("Enter number of rows in pyramid: "))
drawPyramid(rows)

