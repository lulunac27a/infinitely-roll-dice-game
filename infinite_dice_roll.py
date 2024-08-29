"""
Dice game that rolls infinitely number of times until last rolled dice is not 6.
"""
import random #generate random numbers

def roll_dice():
    """
    Rolls the dice.
    """
    return random.randint(1, 6) #roll 6-sized dice
    
def roll_and_multiply():
    """
    Rolls the dice infinite number of times until last rolled dice is not 6, then multiply the rolled dice.
    """
    result = 1 #set result to 1
    roll = roll_dice()# roll the dice
    while roll == 6: #while rolled dice is 6
        result *= 6 #multiply result by 6
        roll = roll_dice() #roll the dice again

    result *= roll #multiply result by last rolled dice
    return result #return the result
    
