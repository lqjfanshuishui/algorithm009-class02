class Solution:
	def maximalSquare(self, matrix: List[List[str]]) -> int:
		if matrix == None or len(matrix) < 1 or len(matrix[0]) < 1:
			return 0
		row = len(matrix)
		col = len(matrix[0])
		matrix_side = 0
		# add one extra column and row to handle the margins
		dp = [[0] * (col + 1) for _ in range(row + 1)]
		for i in range(row):
			for j in range(col):
				if matrix[i][j] == '1':
					dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j + 1], dp[i][j]) + 1
					matrix_side = max(matrix_side, dp[i + 1][j + 1])
		return matrix_side * matrix_side