# #Write a Python program that prompts the user to enter a positive integer and then prints
# all the numbers from 1 to that number using a while loop.


start = int(input("Enter the start of range: ")) 
end = int(input("Enter the end of range: ")) 
  
 
for num in range(start, end + 1): 
  
    
    if num >= 0: 
        print(num, end=" ")