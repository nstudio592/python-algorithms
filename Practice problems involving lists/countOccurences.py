def countOccurences(theList):
    for item in theList:
        count = theList.count(item)
        print("{}:{}".format(item, count))

myList = ["G", "G", 7, 8, 9, 9, 9]
countOccurences(myList)
