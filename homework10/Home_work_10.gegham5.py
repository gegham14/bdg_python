fib1 = fib2 = 1
 
n = input("Fibonacci series element number: ")
n = int(n) - 2
 
while n > 0:
    fib1, fib2 = fib2, fib1 + fib2
    n -= 1
 
print("The value of this element:", fib2)