#  Develop a simple dice rolling simulator. Generate random numbers between 1
# and 6 to simulate the roll of a six-sided die using the random module.
import random

def roll_dice():
   return random.randint(1,6)

print(roll_dice())
