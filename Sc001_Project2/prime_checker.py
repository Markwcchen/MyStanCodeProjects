"""
File: prime_checker.py
Name:Mark
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
	"""
	TODO:check whether the number is a prime number
	"""
	print('Welcome to the prime number')
	while True:
		num = int(input('n: '))
		if num == EXIT:
			print('Have a good one!')
			break
		for i in range(2, num):
			if num % i == 0:
				print(str(num) + ' is not a prime number.')
				break
		else:
			print(str(num)+" is a prime number.")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
