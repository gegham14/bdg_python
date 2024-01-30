#Write a Python function to calculate count of each letter in string


a = "abrakadabra"
b = {}
 
for i in a:
    if i in b:
        b[i] += 1
    else:
        b[i] = 1
 

print("Count of all characters in abrakadabra is :\n "+ str(b))