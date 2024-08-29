import random

def roll_dice(sides):
    return random.randint(1, sides)
    
def roll_and_multiply(sides):
    result = 1
    roll = roll_dice(sides)
    while roll == sides:
        result *= sides
        roll = roll_dice(sides)

    result *= roll
    return result
    
