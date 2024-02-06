"""
File: CollectNewspaperKarel.py
Name: Mark
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    walk to the door and pick up the beeper, and then return to the initial position
    put beeper
    """
    go_out()
    # walk to the door and pick up beeper
    go_home()
    # go home and put beeper


def go_out():
    for i in range(4):
        if front_is_clear():
            move()
        else:
            turn_right()
            move()
            turn_left()
        if on_beeper():
            pick_beeper()
            turn_around()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    for i in range(2):
        turn_left()


def go_home():
    for i in range(4):
        if front_is_clear():
            move()
        else:
            turn_right()
            move()
    turn_right()
    put_beeper()












# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
