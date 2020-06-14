def maxProfit(self, prices: List[int]) -> int:
	profit = 0
	for i in range(1, len(prices)):
		temp_profit = prices[i] - prices[i - 1]
		if temp_profit > 0:
			profit += temp_profit
	return profit