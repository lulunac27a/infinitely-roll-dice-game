import random

def roll_dice():
    return random.randint(1, 6)
    
def roll_and_multiply():
    result = 1
    roll = roll_dice()
    while roll == 6:
        result *= 6
        roll = roll_dice()

    result *= roll
    return result
    
