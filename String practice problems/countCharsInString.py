'''Write a function that counts the number of alphabetic characters (a through z, or A through Z)
in your text and then keeps track of how many are the letter ‘e’. 
Your function should print an analysis of the text:'''
def countChars(string):
    char_count = 0
    for char in string:
        if char == "e":
            char_count += 1
    return char_count

def countAndAverage(string):
    '''returns percentage of string that is letter e'''
    count = countChars(string)
    if count > 0:
        percent = (count / len(string)) *100
        print("The string contains {} characters,  of which {} ({:.2f}%) are the letter e.".format(len(string), count, percent)) 
    else:
        print("The letter e doesn't appear in your string.")

my_string = input("Enter a string: ")
countAndAverage(my_string)
        
    
