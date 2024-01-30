#Write a function that checks if a sentence is a pangram.

def ispangram(x):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in x.lower():
            return False
    return True
string = 'the quick brown fox jumps over the lazy dog'
if(ispangram(string) == True):
    print("true")
else:
    print("false")