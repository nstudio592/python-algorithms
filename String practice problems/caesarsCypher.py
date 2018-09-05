'''Use the Caesar cipher to encrypt a message.
The Caesar cipher works like a substitution cipher but each character
is replaced by the character 13 characters to ‘its right’ in the alphabet.
So for example the letter a becomes the letter n.
If a letter is past the middle of the alphabet then the counting wraps
around to the letter a again, so n becomes a, o becomes b and so on.
Hint: Whenever you talk about things wrapping around its a good idea
to think of modulo arithmetic.'''

def cCypher(msg):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""
    msg = msg.lower()
    for letter in msg:
        if letter == " ":
            encrypted += " "
        else:
            pos = alphabet.index(letter) + 13
            if pos < 26:
                encrypted += alphabet[pos]
            else:
                ecrypted += alphabet[pos%26]
    return encrypted

print(cCypher("ABCDE"))
            
