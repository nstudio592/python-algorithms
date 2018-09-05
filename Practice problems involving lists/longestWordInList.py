'''Write a Python program to find the list of words that are
longer than n from a given list of words.'''
def findLongest(theList, n):
    newList = []
    for word in theList:
        if len(word) >= n:
            newList.append(word)
    if len(newList) == 0:
        return "No item in the list is larger than the number provided."
    return newList

myList = ["The", "dark","elephant","flew","south","previous","winters"]
print(findLongest(myList, 7))
            
