# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 00:26:03 2021

@author: Vitamin-C
"""
from random import randint

class Die():
    """A class representing a die."""
    
    def __init__(self, sides = 6):
        """Assuming a d6."""
        self.num_sides = sides
        
    def roll(self):
        """Returns a random result between 1 and number of die sides."""
        return randint(1, self.num_sides)
    
    