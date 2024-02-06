"""
File: rocket.py
Name: Mark
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.

"""

# This constant determines rocket size.
SIZE = 10


def main():
    """
    TODO: print a rocket
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


# print the top of the rocket
def head():
    for i in range(SIZE):
        for j in range(SIZE-i):
            print(' ', end='')
        for j in range(i + 1):
            print('/', end='')
        # print('')
        for j in range(i + 1):
            print("\\", end='')
        print('')


# print the belt
def belt():
    print("+", end="")
    for i in range(SIZE*2):
        print("=", end="")
    print("+")


# print the upper part of the rocket
def upper():
    for i in range(SIZE):
        print("|", end="")
        for j in range(SIZE-1-i):
            print('.', end="")
        for j in range(i+1):
            print("/\\", end='')
        for j in range(SIZE-i-1):
            print('.', end="")
        print("|", end="")
        print('')


# print the lower part of the rocket
def lower():
    for i in range(SIZE):
        print("|", end="")
        for j in range(i):
            print('.', end='')
        for j in range(SIZE-i):
            print("\\/", end='')
        for j in range(i):
            print('.', end='')
        print("|", end="")
        print('')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
