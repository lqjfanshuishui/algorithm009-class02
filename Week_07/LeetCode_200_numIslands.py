class Solution:
	def  numIsland(self, grid: List[List[str]]) -> int:
		if not grid:
			return 0
		dirctions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
		def  dfs(grid, i, j):
			if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == '0':
				return
			grid[i][j] = '0'
			for d in dirctions:
				dfs(grid, i + d[0], j + d[1])
		count = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == '1':
					count += 1
					dfs(grid, i, j)
		return count
			