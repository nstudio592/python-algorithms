'''Reverse a string'''
def reverseString(string):
    return string[::-1]
    
def isPalindrome(string):
    rev = reverseString(string)
    if string == rev:
        print(string, "is a palindrome")
    else:
        print(string,"is not a palindrome")

s = input("enter a string: ")
isPalindrome(s)
