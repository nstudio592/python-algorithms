'''Write a function that removes the first occurrence of a string from another string.'''
def remove(theStr, substr):
    index = theStr.find(substr)
    if index < 0: # substr doesn't exist in theStr
        return theStr
    return_str = theStr[:index] + theStr[index+len(substr):]
    return return_str

myString = input("Enter a string: ")
mySubstring = input("Enter series of letters to remove from string: ")
print(remove(myString, mySubstring))
