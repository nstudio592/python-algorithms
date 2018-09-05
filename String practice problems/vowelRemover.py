def vowelRemover(a_string):
  '''function to remove vowels from entered string'''
  vowels = "aeiouAEIOU"
  string_without_vowels = ""
  for c in a_string:
    if c not in vowels:
      string_without_vowels += c
  return string_without_vowels
  
my_string = input("Enter a string: ")
print(vowelRemover(my_string))
