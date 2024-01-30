# Write a function that generates a random password for the user. Allow the user
# to specify the length and complexity of the password (include letters, numbers,
# and symbols).


import random
import secrets
import string


letters = string.ascii_letters

digits = string.digits

special_chars = string.punctuation

selection_list = letters + digits + special_chars

password_len = 10

password = " "
for i in range(password_len):
    password+= ''.join(secrets.choice(selection_list))

print(password)