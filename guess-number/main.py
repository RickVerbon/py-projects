import random

exit = False

def getRandomNumber():
    return random.randrange(1, 100);

rndNum = getRandomNumber();

while not exit:
    choice = int(input("Enter a number between 0 and 100: "))
    if(choice < rndNum):
        print("Higher")
    elif(choice > rndNum):
        print("Lower")
    if(choice == rndNum):
        print("You guessed the number right.")