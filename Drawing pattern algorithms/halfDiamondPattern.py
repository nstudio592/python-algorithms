def drawHalfDiamond(n):
	columns = 0
	for i in range(n*2):
		for j in range(columns):
			print("*", end="")
		if(i < n):
			columns += 1
		else:
			columns -=  1
		print()
		
num = int(input("Enter the maximum number of columns in the diamond: "))
drawHalfDiamond(num)

	
