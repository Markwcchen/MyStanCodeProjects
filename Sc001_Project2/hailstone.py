"""
File: hailstone.py
Name:
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    TODO: get the number 1
    """
    print('This program computes Hailstone sequences.')
    count = 0
    n = int(input('Enter a number: '))
    hailstone(n, count)


def hailstone(n, count):
    while True:
        if n == 1:
            break
        elif n % 2 == 0:
            print(str(n), end="")
            n = n // 2
            print(' is even, so I take half: ' + str(n))
            count += 1
        else:
            n % 2 == 1
            print(str(n), end="")
            n = 3 * n + 1
            print(' is odd, so I make 3n+1: ' + str(n))
            count += 1

    print('It took '+str(count)+' steps to reach 1')

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == "__main__":
    main()
