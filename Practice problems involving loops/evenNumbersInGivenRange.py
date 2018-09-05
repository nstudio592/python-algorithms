'''Print even numbers in a given range'''
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

if(start < end):
	print("Numbers between {} and {}".format(start, end))
	for i in range(start, end):
		if(i % 2 == 0):
			print(i)
else:
	print("Numbers between {} and {}".format(end, start))
	for i in range(end, start):
		if(i % 2 == 0):
			print(i)
