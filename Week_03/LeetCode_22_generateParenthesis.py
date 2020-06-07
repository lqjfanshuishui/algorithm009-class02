def generateParenthesis(self, n: int) -> List[str]:

	def _generate(n, left, right, res, s):
		if left == n and right == n:
			res.append(s)
			return

		if left < n:
			_generate(n, left + 1, right, res, s + "(")

		if right < left:
			_generate(n, left, right + 1, res, s + ")")

	res = []
	_generate(n, 0, 0, res, "")

	return res
	