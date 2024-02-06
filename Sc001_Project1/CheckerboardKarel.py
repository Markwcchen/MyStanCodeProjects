"""
File: CheckerboardKarel.py
Name: Mark
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    Arrange beepers in intervals
    """
    put_beeper()
    while left_is_clear():
        fill_one_row()
        if not on_beeper():
            up_left()
            # when facing east, not front is clear, turn left and move
            put_beeper()
        fill_one_row()
        if not on_beeper():
            up_right()
            # when facing west, not front is clear, turn right and move
            put_beeper()
            fill_one_row()


def fill_one_row():
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()


def up_left():
    while facing_east():
        if not front_is_clear():
            turn_left()
            move()
            turn_left()


def up_right():
    while facing_west():
        if not front_is_clear():
            turn_right()
            move()
            turn_right()


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
