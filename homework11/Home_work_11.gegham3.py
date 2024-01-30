# #Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1) 
num = 5
print("Factorial of",num,"is",factorial(num))