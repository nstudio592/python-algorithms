'''Print even numbers in a given range'''
sum = 0
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

if(start < end):
	print("Numbers between {} and {}: ".format(start, end))
	for i in range(start, end):
			sum+=i
else:
	print("Numbers between {} and {}".format(end, start))
	for i in range(end, start):
		sum+=i

print(sum)
