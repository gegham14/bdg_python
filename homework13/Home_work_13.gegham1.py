# Write a Python program to square and cube every number in a given list of
# integers using Lambda

nums = [1, 2, 3, 4, 5,]
print(nums)
print("\n")
square_nums = list(map(lambda x: x ** 2, nums))
print(square_nums)
print("\n")
cube_nums = list(map(lambda x: x ** 3, nums))
print(cube_nums)