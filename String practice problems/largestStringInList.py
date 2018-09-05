'''Write a Python function that takes a list of words
and returns the length of the longest one.'''
listOfWords = ["The", "dog", "likes", "bacon", "shredded"]
largest = ""
for word in range(len(listOfWords)-1):
    if len(listOfWords[word]) < len(listOfWords[word+1]):
        largest = listOfWords[word+1]
print(largest)
