"""
Vasyl Zakharuk
Python Core 355
Codewars Kata. Color Ghost.
"""

# Create a class Ghost
# Ghost objects are instantiated without any arguments.
# Ghost objects are given a random color attribute of white" or "yellow" or "purple" or "red" when instantiated

import random


class Ghost(object):
    def __init__(self, color):
        self.color = random.choice(["white", "yellow", "purple", "red"])


color_ghost = Ghost(object)  # on codewars-site must be empty Ghost()
print(color_ghost.color)
