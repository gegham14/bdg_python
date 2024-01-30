SECRET = "1234"
while True:
   password = input("Enter password: ")
   if password == SECRET:
       print("You got it!")
       break
   else:
       print("Please try again.")