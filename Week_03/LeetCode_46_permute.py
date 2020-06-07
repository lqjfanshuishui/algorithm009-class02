def permute(self, nums: List[int]) -> List[List[int]]:

	def dfs(nums, size, depth, used, path, res):
		if depth == size:
			res.append(path[:])
			return

		for i in range(size):
			if nums[i] not in used:
				path.append(nums[i])
				used.add(nums[i])

				dfs(nums, size, depth + 1, used, path, res)

				path.pop()
				used.remove(nums[i])
	size = len(nums)
	if size == 0:
		return []
	path = []
	res = []
	used = set()
	dfs(nums, size, 0, used, path, res)

	return res