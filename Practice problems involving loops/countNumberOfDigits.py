'''Mathematically count the number of digits in a number'''
count = 0
n = int(input("Enter any number: "))
num = n

while(n >= 1):
	n /= 10
	count += 1
	
print("Number of digits in {} is: {}".format(num, count))
