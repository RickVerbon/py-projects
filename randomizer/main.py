import random
import time

isFound = False
count = 0

inp = input("Choose a number between 1 and 1.000.000: ")
print(f"Randomizing number until i randomized {inp} ")

start = time.process_time()
while not isFound:
    rnd = random.randint(0, 1000000001)
    if(rnd == int(inp)):
        print("---------------------------------------------------------------------")
        print(f"Randomized number: {inp} after {count} tries. This took: {time.process_time() - start} seconds")
        print("---------------------------------------------------------------------")
        
        isFound = True
    else:
        count += 1