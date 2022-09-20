import random
import pyperclip as pc

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
        password = generate_password((int(length)))
        print(f"You can find your new password at your clipboard (Control-V).")
        pc.copy(password)
    elif length == "x":
        exit = True
    else:
        print("Please enter a number")
