from .Generalnumbers import Number_guessing
import random as rd

class Float_numbers(Number_guessing):
    """The computer randomly chooses a float number rounded to two digits between 0 and 1. You make a guess what that number is. 
    The function then tells you if your guess was higher or lower than the actual float number."""

    def __init__(self):
        self.number = round(rd.uniform(0,1), 2)
        self.guess = round(float(input('Please enter your guess: ')), 2)
