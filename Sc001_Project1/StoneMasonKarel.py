"""
File: StoneMasonKarel.py
Name: Mark
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    use beeper to fill the spaces in each column
    """

    turn_left()
    while front_is_clear():
        fill_column()
        turn_left()
        # fill every space in the column
        move_to_next()
        # move to next column


def fill_column():
    while front_is_clear():
        while not on_beeper():
            put_beeper()
        move()
    while not front_is_clear():
        turn_around()
        while not on_beeper():
            put_beeper()
    for i in range(4):
        move()


def move_to_next():
    for i in range(4):
        move()
    turn_left()


def turn_around():
    for i in range(2):
        turn_left()


def turn_right():
    for i in range(3):
        turn_left()










# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
