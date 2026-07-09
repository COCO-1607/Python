Password = input("Enter your password: ")
Password_length = len(Password)

if Password_length < 6:
    print("Your password is weak! Please enter a stronger password.")
elif Password_length <= 10:
    print("Your password is of medium strength.. But it can be better.")
else:
    print("Your password is strong.. That's great!")