'''Given a list of numbers, find and print the first
adjacent elements which have the same sign. 
If there is no such pair, return appropriate message'''
def signOfNeighbors(theList):
    found = False
    for i in range(len(theList)-1):
        if(theList[i] < 0 and theList[i+1] < 0):
            found = True
            print(theList[i], theList[i+1])
    if found == False:
        print("No adjacent elements have the same sign")

myList = [-2, -306, 3, -4]
signOfNeighbors(myList)
