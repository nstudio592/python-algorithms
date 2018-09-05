def reversal(n):
	'''Mathematically determine if a number is a palindrome'''
	reverse = 0
	while(n >= 1):
		remainder = n % 10
		reverse = reverse *10 + remainder
		n //= 10
	return reverse

num = int(input("Enter a number to see if its a palindrome: "))

if(num==reversal(num)):
	print(num, "is a palindrome.")
else:
	print(num, "is not a palindrome")
