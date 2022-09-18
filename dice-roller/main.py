from random import randint

def rollDice(amount):
    dices = []
    for i in range(amount):
        die = randint(1, 6)
        dices.append(die)
    return dices


while True:
    inp = input("Type 'R' or 'r' to roll dices: ")
    if(inp.lower() == "r"):
        amount = input("How many dices would you like to roll?: ")
        if not amount.isnumeric():
            print("Please enter a number above 1")
        elif(int(amount) < 1):
            print("Please enter a number above 1")
        else:
            dicesList = rollDice(int(amount))
            for i in range(6):
                if(i in dicesList):
                    print(f'{i}: You have thrown {dicesList.count(i)}')
                else: 
                    continue