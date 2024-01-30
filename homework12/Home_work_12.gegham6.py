#Write a function that counts the number of words in a sentence.

import re
my_string = "Sam Jan laves axpers? privet *_* !!!" 
print ("The original string is : " + my_string)
res = len(re.findall(r'\w+', my_string))
print ("The number of words: " + str(res))