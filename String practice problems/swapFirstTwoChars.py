'''Write a Python program to get a single string from two given strings,
 separated by a space and swap the first two characters of each string.
 Sample String : 'abc', 'xyz'
 Expected Result : 'xyc abz'
 '''
def swapFirstTwo(string1, string2):
    if len(string1) >= 2 and len(string2) >=2:
        new_string1 = string1[:2] + string2[2:]
        new_string2 = string2[:2] + string1[2:]
        return new_string1 + " " + new_string2 
    else:
        return "Ensure length of both strings is 2 or greater"
        

print(swapFirstTwo("abc", "xyz"))
