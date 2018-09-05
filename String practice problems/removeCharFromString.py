'''Write a Python program to remove the nth index character
from a nonempty string'''
#peanut
def removeChar(string, n):
    first_part = string[:n]
    second_part = string[n+1:]
    return first_part + second_part

my_string = input("Enter a string: ")
index = int(input("Enter index to remove character at that index: "))
print(removeChar(my_string, index))
    
