class Solution:
	def climbStaits(self, n: int) -> int:
		if n == 1:
			return 1
		first = 1
		second = 2
		for i in range(2, n):
			temp = second
			second = first + second
			first = temp
		return second