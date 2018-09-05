'''Given a list of numbers, find and print all the elements 
that are greater than the previous element'''
def greaterThanPrev(theList):
    for i in range(len(theList)-1):
        if theList[i] < theList[i+1]:
            print(theList[i+1])

myList = [77, 801, 54, 609]
greaterThanPrev(myList)
