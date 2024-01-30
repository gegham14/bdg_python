#Input a natural number N and output its last digit 156
n = 156

num_str = repr(n)

last_digit_str = num_str[-1]

last_digit = int(last_digit_str)
print(f"The last digit of {n} is {last_digit}")