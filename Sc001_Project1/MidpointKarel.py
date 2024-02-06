"""
File: MidpointKarel.py
Name: Mark
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    move to the midpoint
    """
    find_total_length()
    # go to end points
    while front_is_clear():
        move()
        if on_beeper():
            pick_beeper()
            turn_around()
            move()
            put_beeper()
    while not front_is_clear():
        turn_around()
        while not on_beeper():
            move()
    while on_beeper():
        pick_beeper()
    put_beeper()


def find_total_length():
    put_beeper()
    while front_is_clear():
        move()
    while not front_is_clear():
        turn_around()
        put_beeper()


def turn_around():
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
