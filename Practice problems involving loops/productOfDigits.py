def productOfDigits(n):
	'''Mathematically calculates the product of digits in a number'''
	product = 1
	while(n >= 1):
		product *= n % 10
		n //= 10
	return product

num = int(input("Enter any number to see the product of its digits: "))
print("Product of digits in {} = {}".format(num, productOfDigits(num)))	
		
