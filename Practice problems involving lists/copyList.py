'''Create a list and make a copy of it.
Return both the orignal list and the copy'''
original_list = []
copied_list =  []

size = int(input("Enter size of list: "))
for i in range(size):
	val = int(input("Enter a value: "))	
	original_list.append(val)

for j in range(size):
	copied_list.append(original_list[j])

print("Original List: ", original_list)
print("Copied List: ", copied_list)
