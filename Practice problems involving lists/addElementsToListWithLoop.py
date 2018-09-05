'''User enters size of list, then adds values to list'''
my_list = []
n = int(input("Enter size of list: "))
for i in range(n):
	val = int(input("Enter value: "))
	my_list.append(val)
print(my_list)
