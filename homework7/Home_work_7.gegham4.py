#Count all letters, digits, and special symbols from a given string
m="P@#yn26at^&i5ve"
Number_count=0
for digits in m:
     if digits.isdigit():
          Number_count+=1
print(Number_count) 