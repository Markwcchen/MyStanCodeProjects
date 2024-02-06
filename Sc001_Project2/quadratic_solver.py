"""
File: quadratic_solver.py
Name: Mark
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	TODO:compute the roots of equation
	"""
	print('stanCode Quadratic Solver!')
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))

	z = b * b - 4 * a * c

	if z > 0:
		y = math.sqrt(z)
		roots = (-b + y) / 2 * a
		roots2 = (-b - y) / 2 * a
		print('Two roots: ' + str(roots) + ',' + str(roots2))
	elif z == 0:
		y = math.sqrt(z)
		roots = (-b + y) / 2 * a
		print('One root: ' + str(roots))
	else:
		z < 0
		print('No real roots ')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
