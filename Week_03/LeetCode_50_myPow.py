def myPow(self, x: float, n: int) -> float:
	def quickPow(N):
		if N == 0:
			return 1.0
		y = quickPow(N // 2)
		return y * y if N % 2 == 0 else y * y * x
	return quickPow(n) if n >= 0 else 1.0 / quickPow(-n)