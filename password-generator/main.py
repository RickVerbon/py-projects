import random

exit = False
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()*+-./:;<=>?"

def generate_password(len):
    newPassword = ""
    for i in range(len):
        rnd = random.choice(chars)
        newPassword += rnd
    return newPassword

while not exit:
    length = input("Length of the password: ")
    if(length.isnumeric()):
        print(f"Your new password is: {generate_password((int(length)))}")
    elif length == "x":
        exit = True
    else:
        print("Please enter a number")
