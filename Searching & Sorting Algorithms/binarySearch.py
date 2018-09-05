def binarySearch(target, array):
    bottom = 0
    top = len(array)-1
    while bottom <= top:
        middle = (bottom+top)//2
        if array[middle] == target:
            return middle
        elif array[middle] < target:
            bottom = middle + 1
        else:
            top = middle - 1
    return "Number not found"

myArray = [1, 2, 3, 4, 5, 6]
key = int(input("Enter a number to search for: "))

print(binarySearch(key, myArray))
