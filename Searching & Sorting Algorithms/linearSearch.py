def linearSearch(target, array):
    position = 0
    found = False
    while position < len(array) and not found:
        if array[position] == target:
            found = True #loop continues until last line of loop or return statement
            return position #return breaks the loop
        position += 1
    return "Target not found"

def altLinearSearch(target, array):
    for position in range(len(array)):
        if array[position] == target:
            return position
    return "Target not found"
    

myArray = [77, 99, 304, 365, 90210, 811, 666]
print(linearSearch(811, myArray))
print(altLinearSearch(90210, myArray))
