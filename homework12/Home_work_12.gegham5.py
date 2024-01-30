#Write a function that calculates the sum of squares of numbers from 1 to n.

N = int(input("Enter value of N: "))
sumVal = 0

for i in range(1, N+1):
    sumVal += (i*i)

print("Sum of squares = ", sumVal)