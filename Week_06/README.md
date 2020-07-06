## Week 06 学习笔记
### 分治 递归 回溯的回顾
* 很多问题都有自相似性，所以可以把大的问题分解成小的子问题去解决。
* 递归的模版： 1. 递归终止条件 2. 处理当前层逻辑 3. 进入到下一层
* 关键是找到可以拆解为可重复解决的问题
* 数学归纳法的思想：n = 0, n = 1 成立 n = n, n = n + 1也成立

### 动态规划 dynamic programming

* dp 和 分治是有联系的， 分治 + 最优子结构的组合
* 中途可以淘汰次优解

### 实战例题

* fibonacci sequence
	*  没有缓存的递归：复杂度为 2^n (call tree has n levels, all together is 2^n）
	*  自顶向下： 从fib(6) 开始计算
	*  Bottom Up: 转化为循环
	
	``` python
	F[n] = F[n - 1] + F[n - 2]
	a[0] = 0, a[1] = 1
	for i in range(2, n + 1):
		a[i] = a[i - 1] + a [i - 2]
	return a[n]   
	```
	
* 路径计数
	*  状态转移方程
	*  opt[i, j] = opt[i + 1, j] + opt[i, j + 1]
* 最长公共子序列
	* 把两个单词分别放在 行 和 列上面
	* if a[i - 1] == b[j - 1]: dp[i][j] = dp[i - 1][j - 1] + 1
	* else: dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
* 三角形最小路径和
	* 重复性：sub(i, j)  = min(sub(i + 1, j), sub(i + 1, j + 1)) + a[i, j]
	* 定义状态数组：f[i, j]
	* dp：f(i, j)  = min(f[i + 1, j], f[i + 1, j + 1]) + a[i, j]
* 最大子序和
	* 子问题：max\_sum(i) = max(max\_sum(i - 1), 0) + a[i]
	* 状态数组定义：f[i]
	* dp方程：  f[i] = max(f[i - 1], 0) + a[i] 
