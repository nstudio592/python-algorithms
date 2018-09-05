'''Given a list of unique numbers, swap the minimal
and maximal elements of this list. Print the resulting list.'''
def swapMinMax(theList):
    largest = max(theList)
    smallest = min(theList)
    
    smallestIndex = theList.index(smallest)
    largestIndex = theList.index(largest)
    
    temp = theList[smallestIndex]
    theList[smallestIndex] = theList[largestIndex]
    theList[largestIndex] = temp
    
    return theList

myList = [33, 509, 644, 399, 875]
print(swapMinMax(myList))
    
    
        
