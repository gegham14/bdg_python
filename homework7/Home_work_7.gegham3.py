#Arrange string characters such that lowercase letters should come first
def balance(PYnative,Yn):
    flag=True

    if (len(PYnative) == len(Yn)):
        for i in PYnative:
            if i in Yn:
                continue
            else:
                flag = False

        return flag

PYnative = input()
Yn = input()

if balance(PYnative, Yn) == True:
    print("True")
else:
    print("False")