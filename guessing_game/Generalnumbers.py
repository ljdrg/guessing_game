import random as rd

class Number_guessing:
    """Number guessing game. The computer selects a random number and you have to guess it. It will give hints
    telling you if its number is higher or lower than your guess"""


    def __init__(self):
        self.number 
        self.guess 

    def check(self):
        if self.number > self.guess:
            return f'The number is higher than your guess.'
        elif self.number < self.guess:
            return f'The number is lower than your guess.'
        else:
            return 'Congrats you guessed the correct number!'
        
    def try_again(self):
        self.guess = int(input('Please enter a new guess: '))
        
    # def make_guess(self, self.guess):
