'''Write a Python program to get a string from a given string where all occurrences of 
its first char have been changed to '$', except the first char itself.'''
def changeCharacters(string):
    first_char = string[0] #isolate first character
    string = string.replace(first_char, "$") #replace occurrences of first char
    string = first_char + string[1:] #add first char to string with replaced chars
    return string

my_string = input("Enter a string: ")
print(changeCharacters(my_string))
        
        
        
    
