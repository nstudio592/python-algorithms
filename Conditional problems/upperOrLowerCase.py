def upperOrLower1(ch):
	'''First method to determine if a letter is uppercase
	 or lowercase using inbuilt functions'''
	if(len(ch) > 1):
		print("Sorry, you entered a word not a letter.")
	elif(ch.upper() == ch):
		print(ch, "is uppercase")
	else:
		print(ch, "is lowercase")

def upperOrLower2(ch):
	'''Second method to determine if a number is upper or lower case
	This method uses unicode value of letter instead of inbuilt function
	'''
	if(len(ch) > 1 or len(ch) < 0):
		print("Sorry, please enter a single letter.")
	elif(ch >= 'A' and ch <= 'Z'):
		print(ch, "is uppercase")
	elif(ch >= 'a' and ch <= 'z'):
		print(ch, "is lowercase")

letter = input("Enter a letter: ")
#upperOrLower1(letter) uncomment this function to try it out
upperOrLower2(letter) 
