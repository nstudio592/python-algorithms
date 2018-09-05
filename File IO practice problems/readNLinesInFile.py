'''Program to n number of lines in a file where n is a value
entered by the user'''
n = int(input("Enter number of lines: "))
count = 0

with open("test.txt", "r") as f:
	for line in f:
		print(line, end="")
		count = count + 1
		if count >= n:
			break
		
