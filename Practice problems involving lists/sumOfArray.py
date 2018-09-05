'''Find sum of items in a list'''
my_list = []

def createList():
	size = int(input("Enter size of list: "))
	for i in range(size):
		value = int(input("Enter item into the list: "))
		my_list.append(value)
	return my_list

createList()

sum = 0
for i in range(len(my_list)):
	sum = sum + my_list[i]
print("Sum of {} is {}".format(my_list, sum))
