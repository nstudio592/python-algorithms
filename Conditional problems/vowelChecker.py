'''Program to check if letter is vowel or consonant'''
string = "AEIOUaeiou"
ch = input("Enter a letter: ")

if(ch in string):
	print("{} is a vowel".format(ch))
elif(ch not in string):
	print("{} is a consonant".format(ch))
else:
	print("Sorry, you didn't enter a letter.")
