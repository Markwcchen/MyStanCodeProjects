"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	# 負數取絕對值
	n = abs(n)

	# 個位數可以直接 return
	if n < 10:
		return n
	# 去除尾數 先比較其他位數
	max_ = find_largest_digit(n//10)

	# 取尾數
	last_digit = n % 10

	return max(last_digit, max_)


if __name__ == '__main__':
	main()
