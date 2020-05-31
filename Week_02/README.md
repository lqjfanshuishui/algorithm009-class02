# Week 02 学习笔记

### 哈希表 映射 集合

* 哈希表也叫散列表， 通过关键码值来进行直接访问的数据结构。
* 通过hash function来计算出hashcode 找到在对应表中的位置来存储。常见的哈希函数可以是 取一个质数的余数 （mod p）。
* 如果两个key value经过hash function计算后得到的hashcode是一样的话就会造成储存的时候的碰撞， 这个时候就要在对应的位置上再拉一个链表出来去处理碰撞。
* 还有其他处理碰撞的办法比如用另外一个hash function再hash一遍。或者去找发生碰撞的下一个空位去储存。好的哈希函数会使碰撞尽可能少的发生。使得查询的平均时间复杂度为 O(1)。
* java 里的的哈希表经常使用的是map 和set。
* map : key - value 对， key不重复
* set : 不重复元素的集合

### 树 二叉树 二叉搜索树

* 树和图最重要的差别就是树没有环。

``` python
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None
```

* 现实中的很多问题的不同的状态扩散出去就是一个树形的结构，所以树这种结构可以很自然的去表示很多问题的不同的状态。
* 树的结构导致了树没有很简单的方法实现循环遍历。而且树的结构也有一定的重复性，每个子树单独拿出来都是一个树，而递归性的问题也具有这个特点，所以有关树的算法很多时候都会选择使用递归去解决。
*  树的遍历
	* pre-order : root , left , right
	
	```python
	def preOrder(self, root):
		if root:
			self.traverse_path.append(root.val)
			self.preOrder(root.left)
			self.preOrder(root.right)
	```
	* in-order : left, root , right
	
	```python
	def inOrder(self, root):
		if root:
			self.inOrder(root.left)
			self.traverse_path.append(root.val)
			self.inOerder(root.right)
	```
	* post-order : left, right, root  

	```python
	def postOrder(self, root):
		if root:
			self.postOrder(root.left)
			self.postOrder(root.right)
			self.traverse_path.append(root.val)
			
	```
	
* 二叉搜索树的性质：
	* 左子树上的**所有节点**的值均小于它的根节点
	* 右子树上的**所有节点**的值均大于它的根节点
	* 以此类推：左，右子树也分别为二叉搜索树。
* 二叉搜索树的中序遍历为升序排列。
* 二叉搜素树的查询，插入和删除都为 O(logN) ，n 为树的节点数。
* 删除相对复杂 **to do**

### 堆（heap）二叉堆（binary heap）

*  特点： 可以迅速找到一堆数中的最大值和最小值的数据结构。
*  现实中会不断的有新的数据产生和一些数据的删除，如果需要动态的找到最大值或者最小值就需要用到堆。用数组的和排序的话每次都要重新进行排序，用堆的话只要按照规则插入就可以了。
*  find-max:  O(1) delete-max: O(logN) insert(creat): O(logN) or O(1)
*  二叉堆通过**完全二叉树来实现** 
	*  因为是完全二叉树所以一般通过数组来实现
	*  假设第一个元素在数组中的索引为0，则父节点和子节点的位置关系如下：
		* 索引为**i**的左孩子的索引为**(2*i+1)** 
		* 索引为**i**的左孩子的索引为**(2*i+2)**
		* 索引为**i**的父节点的索引是 **floor((i-1)/2)**

* 插入操作：
	* 新元素一律先插入到堆的尾部。
	* 再一次向上整理堆的结构。
	* heapifyUp O(logN)
* 删除操作：
	*  将堆尾的元素替换道顶部
	*  依次向下整理堆的结构
	*  heapifyDown O(logN)