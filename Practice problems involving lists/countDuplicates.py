'''Pyhon program to count duplicate items in list'''
def countDuplicates(theList):
    count = 1
    for i in range(len(theList)):
        for j in range(i+1, len(theList)):
            if theList[i] == theList[j]:
                count += 1
                break
    print("Number of duplicate elements:", count)

myList = [27, 27, 33, 44, 27, 27, 44]
countDuplicates(myList)

