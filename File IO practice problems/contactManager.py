'''Contacts manager program'''

def main():
	print("Contacts Manager")
	
	#Initialize friends list
	friends = []
	fr = open("contacts.txt", "r")
	line = fr.readline()
	while line:
		friends.append(line.rstrip("\n").split(","))
		line = fr.readline()
	fr.close()
	
	choice = 0
	while choice != 4:
		print("1) Add friend")
		print("2) Look up a friend")
		print("3) Display all friends")
		print("4) Quit")
		choice = eval(input())
		
		if choice == 1:
			print("Adding a friend")
			name = input("Enter name: ")
			email = input("Enter email: ")
			phone = input("Enter phone number: ")
			friends.append([name, email, phone])	
			
		elif choice == 2:
			print("Look up a friend")
			keyword = input("Enter keyword to search: ")
			for friend in friends:
				if keyword in friend:
					print(friend)
					
		elif choice == 3:
			print("Displaying all friends")
			for i in range(len(friends)):
				print(friends[i])
		elif choice == 4:
			print("Quitting program")

		else:
			print("Invalid response")
	
	fw = open("contacts.txt", "w")
	for friend in friends:
		fw.write(",".join(friend) +"\n")
	fw.close()
	
	print("Program terminated")

main()
