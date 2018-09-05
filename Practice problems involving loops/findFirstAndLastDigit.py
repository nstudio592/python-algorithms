def findLastDigit(n):
	'''Mathematically finds the last digit of a number'''
	lastDigit = n % 10
	return lastDigit

def findFirstDigit(n):
	'''Mathematically finds the first digit of a number'''
	first = n
	while(first >= 10):
		first //= 10
	return first

num = int(input("Enter any number: "))
print("First Digit: ", findFirstDigit(num))
print("Last Digit: ", findLastDigit(num))


