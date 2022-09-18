import random

exit = False

def getRandomNumber():
    return random.randrange(1, 100);

rndNum = getRandomNumber()

while not exit:
    choice = input("Enter a number between 0 and 100, enter 'x'  to quit: ")
    if(choice.isnumeric()):
        if(int(choice) >= 0 or int(choice) <= 100):
            if(int(choice) < rndNum):
                print("Higher")
            elif(int(choice) > rndNum):
                print("Lower")
            elif(int(choice) == rndNum):
                print("You guessed the number right.")
                print("______________________________")
                print("Generated new number")
                rndNum = getRandomNumber()
            else:
                continue
    elif(choice == 'x'):
        exit == True
    else: 
        print("Invalid input, please enter a number to play, or 'x' to quit")
        