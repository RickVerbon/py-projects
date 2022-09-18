import random

exit = False

choices = ["Rock", "Paper", "Scissors"]

while not exit:
    opponentChoice = random.choice(choices)
    playerChoice = input("Rock, paper, scissors?: ")

    if(playerChoice == opponentChoice):
        print("It's a draw")
        print("")
    elif((playerChoice == "Rock" and opponentChoice == "Scissors") or (playerChoice == "Paper" and opponentChoice == "Rock") or (playerChoice == "Scissors" and opponentChoice == "Paper")):
        print(f"{playerChoice} beats {opponentChoice}, player won.\n")
        print("")
    elif(playerChoice == 'x'):
        exit = True
    else:
        print(f"{opponentChoice} beats {playerChoice}, computer won.")
        print("")
        


