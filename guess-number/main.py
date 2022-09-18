import random

exit = False

def getRandomNumber():
    return random.randrange(1, 100);

rndNum = getRandomNumber()

while not exit:
    choice = int(input("Enter a number between 0 and 100, enter '-1'  to quit: "))
    if(choice < rndNum):
        print("Higher")
    elif(choice > rndNum):
        print("Lower")
    elif(choice == rndNum):
        print("You guessed the number right.")
        rndNum = getRandomNumber()
    elif(choice == -1):
        exit = True
    else:
        print("Wrong input")