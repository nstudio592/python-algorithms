'''Write a function that removes all occurrences of a string from another string'''
def removeAll(string, substring):
    newString = string.replace(substring, "")
    return newString

myString = input("Enter a string: ")
mySubString = input("Enter substring to remove all occurences of it from original string: ")
print(removeAll(myString, mySubString))
