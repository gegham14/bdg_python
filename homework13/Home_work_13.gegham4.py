# Write a Python program to find intersection of two given arrays using
# Lambda

def interSection(arr1 ,arr2):
    result = list(filter(lambda x: x in arr1, arr2))
    print ("Intersection : " ,result)
if __name__ == "__main__":
    arr1 = [1, 2, 3, 5, 7, 8, 9, 10]
    arr2 = [1, 2, 4, 8, 9]
    interSection(arr1 ,arr2)
print(arr1)
print (arr2)