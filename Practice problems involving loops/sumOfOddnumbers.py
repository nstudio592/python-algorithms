'''Find sum of odd numbers from 1 to n inclusive'''
n = int(input("Enter number: "))
sum = 0

print("Sum of odd numbers from 1 to {}:".format(n))
for i in range(n+1):
	if(i % 2 != 0):
		sum += i
print(sum)

