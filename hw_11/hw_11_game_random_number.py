"""
Vasyl Zakharuk
Python Core 355
Home work 11. Game: random number.
"""


import random
robot_chappy = random.randint(1, 100)  # because I like him
human_user = int(input("Please input your number: "))  # this's me or anybody else
while human_user != robot_chappy:
    if human_user < robot_chappy:
        print("The number is too small!")
    elif human_user > robot_chappy:
        print("The number is too large!")
    human_user = int(input("Please input your number: "))
print("You have selected the correct number!")
