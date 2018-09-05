'''print all negative numbers in a list'''
my_list = [473, -79, 438, 8960, -954, -54]
negative_list = []
for i in range(len(my_list)):
	if my_list[i] < 0:
		negative_list.append(my_list[i])
	
print(negative_list)
