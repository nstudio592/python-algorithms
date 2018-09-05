def sumOfDigits(n):
	'''mathematically calculate the sum of digits in a number'''
	sum = 0
	while(n >= 1):
		sum += n % 10 #adds last digit of sum to num
		n //= 10 #removes last digit from number
	return sum

num = int(input("Enter any number to see the sum of its digits: "))
print("Sum of digits in {} = {}".format(num, sumOfDigits(num)))	
		
