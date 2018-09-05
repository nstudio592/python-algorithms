'''find largest and smallest values in a list'''
def findLargest(theList):
    largest = theList[0]
    for i in range(len(theList)-1):
        if theList[i] < theList[i+1]:
            largest = theList[i+1]
    return largest

def findSmallest(theList):
    smallest = theList[0]
    for i in range(len(theList)):
        if theList[i] < smallest:
            smallest = theList[i]
    return smallest

my_list = [239, 445, 643, 204, 667, 87]
print(findLargest(my_list))
print(findSmallest(my_list))
