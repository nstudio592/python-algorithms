n = int(input("Enter number to generate its multiplication table: "))
for i in range(1,13):
	print("{} x {} = {}".format(n, i, n*i))
