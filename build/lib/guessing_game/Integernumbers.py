from .Generalnumbers import Number_guessing
import random as rd

class Integer_numbers(Number_guessing):
    """The computer randomly chooses an integer number between 0 and 10. You make a guess what that number is. 
    The function then tells you if your guess was higher or lower than the actual float number."""
    def __init__(self):
        self.number = rd.randint(0,10)
        self.guess = int(input('Please enter your guess: '))