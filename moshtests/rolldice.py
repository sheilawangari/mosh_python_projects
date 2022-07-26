# getting a random two numbers when we roll the dice

import random

class Dice:
    def roll(self):
        first = random.randint(1, 6)   # this randomly generates numbers for the first side
        second = random.randint(1, 6)  # this for second

        return first, second    # you can use tuple () or no tuple


dice = Dice()
print(dice.roll())
