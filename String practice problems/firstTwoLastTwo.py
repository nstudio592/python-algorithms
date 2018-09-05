'''Write a Python program to get a string made of
the first 2 and the last 2 chars from a given a string. If the string length is less than 2,
return instead of the empty string'''
def firstAndLastTwo(string):
    new_string = ""
    if len(string) >= 2:
        first_two = string[:2]
        last_two = string[len(string)-2:]
        return first_two + last_two
    else:
        return "String is too small"

my_string = input("Enter a string: ")
print(firstAndLastTwo(my_string))
