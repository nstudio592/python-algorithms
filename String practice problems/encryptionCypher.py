'''Write a function that implements a substitution cipher.
In a substitution cipher one letter is substituted for another to garble the message.
For example A -> Q, B -> T, C -> G etc.
your function should take two parameters, the message you want to encrypt,
and a string that represents the mapping of the 26 letters in the alphabet.
Your function should return a string that is the encrypted version of the message.'''
def encrypt(msg, cypher):
    alphabet = 'abcdefghijklmnopqqrstuvwxyz'
    encrypted = ""
    for letter in msg:
        if letter == " ":
            encrypted += " "
        else:
            pos = alphabet.index(letter)
            encrypted = encrypted + cypher[pos]
    return encrypted
    
'''Write a function that decrypts the message from the previousfunction.
It should also take two parameters. The encrypted message, and the mixed up alphabet.
The function should return a string that is the same as the original unencrypted message.'''
def decrypt(msg, cypher):
    alphabet = 'abcdefghijklmnopqqrstuvwxyz'
    decrypted = ""
    for letter in msg:
        if letter == " ":
            decrypted += " "
        else:
            pos = cypher.index(letter)
            decrypted += alphabet[pos]
    return decrypted

myCypher = "badcfehgjilknmporqtsvuxwzy"
myMessage = "rattle snake"
encrypted = encrypt(myMessage, myCypher)
print(encrypted)
print(decrypt(encrypted, myCypher))
