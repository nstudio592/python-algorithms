'''Write a Python program to add 'ing' at the end of a
 given string (length should be at least 3). If the given string already ends with 'ing' 
then add 'ly' instead. If the string length of the given string
is less than 3, leave it unchanged.'''
def addSuffix(string):
    if len(string) >= 3:
        if(string[len(string)-3:] =="ing"):
            print(string + "ly")
        else:
            print(string + "ing")
    else:
        print("Sorry, the string you entered is too short.")

addSuffix("x")
addSuffix("xyz")
addSuffix("boring")
