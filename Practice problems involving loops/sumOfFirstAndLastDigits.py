def findLastDigit(n):
	'''Mathematically finds the last digit of a number'''
	last = n % 10
	return last

def findFirstDigit(n):
	'''Mathematically finds the first digit of a number'''
	first = n
	while(first >= 10):
		first //= 10
	return first

num = int(input("Enter any digit: "))
total = findLastDigit(num) + findFirstDigit(num)

print("Sum of first and last digits:", total)
