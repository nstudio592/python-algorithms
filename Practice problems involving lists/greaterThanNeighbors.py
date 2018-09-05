'''Given a list of numbers, determine and print the quantity of elements
that are greater than both of their neighbors.
The first and the last items of the list shouldn't be considered
because they don't have two neighbors.'''
def greaterThanNeighbors(theList):
    count = 0
    for i in range(1, len(theList)-1):
        if theList[i] > theList[i+1] and theList[i] > theList[i-1]:
            count = count + 1
    print(count)

myList = [1, 5, 1, 5, 1]
greaterThanNeighbors(myList)
