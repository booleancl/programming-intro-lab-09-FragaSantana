import random

class Dice:
    def roll(self):
        #return random.choice(range(1,2,3,4,5,6))
        return random.randrange(1,6)

