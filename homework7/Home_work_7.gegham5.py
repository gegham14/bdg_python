#Count all letters, digits, and special symbols from a given string
m="P@#yn26at^&i5ve"
latter_count=0
for chars in m:
     if chars.isalpha():
          latter_count+=1
print(latter_count)
