## Week 04 学习笔记

### Breadth First Search and Depth First Search

* 树和图的搜索：
	* 每个节点都要访问一次
	* 并且每个节点仅访问一次  
* DFS template (递归实现， 栈实现)

```python
# recursive
visited = set()

def dfs(node, visited):
	if node in visited: #terminator
		#already visited
		return
	
	visited.add(node)
	
	#process current node here.
	...
	for next_node in node.children():
		if next_node not in visited:
			dfs(next_node, visited)
```
```python
def DFS(self, tree):

	if tree.root is None:
		return []
	visited, stack = [], [tree.root]
	while stack:
		node = stack.pop()
		visited.add(node)
		
		process(node)
		
		nodes = genereate_related_nodes(node)
		stack.push(nodes)
```

* BFS 队列实现 
* BFS Template

```python
def BFS(graph, start, end):

	queue = []
	queue.append([start])
	visited.add(start)
	
	while queue:
		node = queue.pop()
		visited.add(node)
		
		process(node)
		
		nodes = generate_related_nodes(node)
		queue.push(nodes)
```