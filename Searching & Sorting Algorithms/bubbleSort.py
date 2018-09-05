def bubbleSort(array):
    #Outer loop controls num times swapping occurs
    for i in range(0, len(array)-1):
        #Inner loop performs swaps for each element in list
        #less swaps to do each time since last element is in right position
        for j in range(0, len(array)-1-i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

myList = [88, 704, 32, 99, 1]
print(bubbleSort(myList))
