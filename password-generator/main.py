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
    length = int(input("Length of the password: "))
    print(f"Your new password is: {generate_password((length))}")
