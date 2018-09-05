def reverseNumber(n):
	reverse = 0
	while(num >= 1):
		reverse = reverse * 10
		reverse = reverse + n % 10
		n //= 10
	return reverse

num = int(input("Enter any number to see its reverse: "))
print("Reverse of {} = {}".format(num, reverseNumber(num)))
