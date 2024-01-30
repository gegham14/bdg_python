# Write a Python program to check whether a given string is number or
# not using Lambda.

def is_numeric(string: str) -> bool:

    try:
        float(string)
        return True

    except ValueError:
        return False
print(is_numeric("28"))
print(is_numeric("a"))
print(is_numeric("21"))
print(is_numeric("12ab12"))