'''Write a Python program to print the numbers of a specified
list after removing even numbers from it'''
def removeEvenNums(theList):
    newList = []
    for i in range(len(theList)):
        if theList[i] % 2 != 0:
            newList.append(theList[i])
    return newList

def altMethod(theList):
    '''For loop cant be used in this method because the range function
    calculates the length of the list before the program starts, and does
    not update it through each iteration'''
    i = 0
    while i < len(theList):
        if theList[i] % 2 == 0:
            theList.pop(i)
        else:
            i += 1
    return theList

myList = [88, 66, 44, 88, 22, 100]
print(removeEvenNums(myList))
print(altMethod(myList))
