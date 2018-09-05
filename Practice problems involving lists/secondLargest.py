'''find largest and second largest element in an array.'''
def secondLargest(theList):
    largest = max(theList)
    secondBiggest = 0
    for i in range(len(theList)):
        if secondBiggest < theList[i] and theList[i] < largest:
            secondBiggest = theList[i]
    return secondBiggest

myList = [304, 1, 27]
print(secondLargest(myList))

    
