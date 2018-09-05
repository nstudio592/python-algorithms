'''For numbers between 1 to n, print fizz for multiples of 5
print buzz for multiples of 7'''
n = int(input("Enter any positive whole number: "))
for i in range(n):
	if(i % 5 == 0):
		print("Fizz")
	elif(i % 7 == 0):
		print("Buzz")
