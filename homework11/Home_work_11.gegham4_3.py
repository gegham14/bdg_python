# Write a python function, which create a dictionary
# for given number N, where keys are numbers from
# 1 to N, and values are cubs of that numbers

d = dict()
for x in range(1, 16):
    d[x] = x ** 2
print(d)