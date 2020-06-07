## Week 03 学习笔记

### 递归
* 递归代码模版

``` python
def recursion(level, param1,  param2, ...):
	# recursion terminator
	if level > MAX_LEVEL:
		process_result
		return
	
	# process logic in current level
	process(level, data...)
	
	# drill down
	self.recursion(leve + 1, param1, param2, ...)
	
	# reverse the current level status if needed

``` 
* 递归的关键就是找到**最近重复子问题**，基本上所有的程序都只包括 if.. else.. 循环 和递归调用三部分。
* 数学归纳法的思维：基本的情况成立可以泛化到所有的情况都可以这样解决。n = 1， n = 2 成立，并且 n 的时候成立可以推导到n + 1的时候也成立。

### 分治 回溯

*  分治和回溯是特殊的递归
*  分治的特殊的地方是合并的时候有时候会做一些操作。

