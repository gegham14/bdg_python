#Arrange string characters such that lowercase letters should come first

a="PyNaTive"
s="".join(sorted(a))
print(s[::-1])