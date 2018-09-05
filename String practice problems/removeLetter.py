'''Remove occurrences of a given number'''
def removeLetter(string, letter):
    if letter in string:
        return string.replace(letter, "")
    else:
        return "That letter doesn't occur in the string."

myString = input("Enter a word/sentence: ")
ch = input("Enter a letter to remove from word/sentence: ")
print(removeLetter(myString, ch))
    
