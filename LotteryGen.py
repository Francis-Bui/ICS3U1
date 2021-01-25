import random

# Constants
min = 1
max = 49

# Variables
randomNum = 0
winner = 0
count = 0

name = str(input("What's your name?"))
max = int(input("What is the MAXIMUM range?"))

# Looping our number generation until it happens six times
while count < 6:
    count += 1
    randomNum = random.randrange(min, max)
    print(randomNum)

# Instead of making another number generator we can take our pre existing numbers and divide by 4
if count == 6 and randomNum < 13:
    print(f"You're a winner {name}!")
else:
    print(f"Better luck next time {name}!")