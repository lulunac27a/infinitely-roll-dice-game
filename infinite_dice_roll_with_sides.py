"""
Dice game that rolls infinitely number of times until last rolled dice is not the number of sides of the dice.
"""

import random  # generate random numbers


def roll_dice(sides):
    """
    Rolls the dice with specified number of sides.
    sides - the number of sides to roll.
    """
    return random.randint(1, sides)  # roll the dice with specified number of sides


def roll_and_multiply(sides):
    """
    Rolls the dice infinite number of times until last rolled dice is not the number of sides of the dice, then multiply the rolled dice.
    sides - the number of sides to roll.
    """
    result = 1  # set result to 1
    roll = roll_dice(sides)  # roll the dice with specified number of sides of dice
    while roll == sides:  # while rolled dies is not the number of sides of dice
        result *= sides  # multiply result by number of sides of dice
        roll = roll_dice(sides)  # roll the dice again

    result *= roll  # multiply result by last rolled dice
    return result  # return the result
