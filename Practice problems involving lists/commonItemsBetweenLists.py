'''Write a Python function that takes two lists and
returns True if they have at least one common element'''
def findCommonItems(listA, listB):
    flag = False
    for i in listA:
        for j in listB:
            if i == j:
                flag = True
                return "There are common items between the 2 lists"
    if flag == False:
        return "The 2 lists have no items in common"
    
            
myListA = [7, 8, "wild", "dogs", 28]
myListB = [33, 24, 8, "cat", "clouds"]
print(findCommonItems(myListA, myListB))
