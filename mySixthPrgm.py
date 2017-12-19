password = ""
while password != "pyhton123":
    password = input("Enter the password: ")
    if(password == "python123"):
        print("You are logged in successfully!!")
    else:
        print("You have entered wrong password, sorry try again!!")
