"""
File: weather_master.py
Name:Mark
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
QUIT = -100


def main():
	"""
	TODO: find the highest, lowest and average temperature
	"""
	print('stanCode \"Weather Mater 4.0\"!')
	temp = int(input('Next Temperature: (or -100 to quit)? '))
	cold_day = 1
	days = 1
	sum_temp = temp
	average = sum_temp // days

	if temp == QUIT:
		print('No temperatures were entered')

	else:
		maximum = temp
		minimum = temp
		while True:
			temp = int(input('Next Temperature: (or -100 to quit)? '))
			if temp == QUIT:
				break
			if maximum < temp:
				maximum = temp
				days += 1
				sum_temp += temp
			elif minimum > temp:
				minimum = temp
				days += 1
				sum_temp += temp

			if temp < 16:
				cold_day += 1

		print('Highest temperature = ' + str(float(maximum)))
		print('Lowest temperature = ' + str(float(minimum)))
		print('Average = ' + str(float(sum_temp//days)))
		print(str(int(cold_day))+' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == "__main__":
	main()
