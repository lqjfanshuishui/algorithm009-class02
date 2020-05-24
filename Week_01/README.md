

##Week 01 学习笔记

### 数组 链表 跳表
1. 数组

	* 申请数组的时候是在内存中开辟了一段连续的地址。
	* 特性：访问数组中的任意元素时间复杂度为 O(1)。
	* 插入操作和删除操作时间复杂度比较高为 O(n)。
	* 插入时需要挪动插入位子后面的元素，删除就需要前挪。
	* java ArrayList 底层实现 需要用arraycopy实现挪动。
2. 链表
	* 在增加删除的操作比较频繁的时候比较数组好的数据结构。
	* 只有一个next指针为单链表，如果还有一个previous指针的话为双向链表。
	* 头指针head， 尾指针tail。 tail指向 null， 如果tail 指向头的话为循环链表。
	* java中的链表为双向链表。
	* 链表增加删除操作的时间复杂度为O(1)，访问任意位置的时间复杂度为O(n)。

3. 跳表
	* 对于链表的优化
	* 跳表的很重要的前提是，**链表里的元素是有序的**。
	* 插入/删除/搜索 都是O(log n)的数据结构。
	* 优化思想：一维数据结构升维，空间换时间。
	* 链表的实现： 加多级索引。索引的高度为 log2n。
	* 现实中的跳表，索引并不整齐，因为每次增加删除操作需要更新索引，维护成本较高。

### 栈 队列 双端队列 优先队列
1. 栈
	* 先入后出
	* 添加删除为O(1)。 查询为O(n)。

2. 队列
	* 先入先出
	* 添加删除为O(1)。 查询为O(n)。

3. 双端队列(Double-End Queue)
	* 两端都可以进出的Queue
	* 插入和删除操作都是O(1)。

4. 优先队列
	* 插入操作为O(1), 取出操作为O(log n)。
	* 底层实现可能为heap, bst, treap。

	
``` java
 Deque<String> deque = new LinkedList<String>();
 
 deque.addFirst("a");
 deque.addFirst("b");
 deque.addFirst("c");
 System.out.println(deque);
 
 String str = deque.peekFirst();
 System.out.println(str);
 System.out.println(deque);
 While (deque.size() > 0) {
 	System.out.println(deque.removeFirst());
 }
 System.out.println(deque);
 
```

### Java Queue and PriorityQueue Source Code Review

#### Queue

Queue in java is an interface which extends Collection. It has six abstract methods need to be implemented.


```java 
boolean add(E e);
```

*  parameter **e** is the element to add. It will return true if the element is add to the queue successfully, if there is no space in the queue is available it will throw an IllegalstateException.


```java 
boolean offer(E e);
```

*   parameter **e** is the element to add, and the return boolean value indicates that weather the element was added to this queue or not. 

```java 
E remove();
```

*  It returns the head of this queue and remove it. The only difference between this methon and **poll** is that, this method would throw an exception if the queue is empty.


```java 
E poll();
```

* Retrieves and removes the head of this queue, or returns null is this queue is empty.

```java 
E element();
```

* Retrieves , but does not remove, the head of this queue, The difference between **peek** is that, this method would throw an exception if this queue is empty.

```java 
E peek();
```

* Return the head of this queue and return null if this queue is empty.

#### PriorityQueue


```java 
Class PriorityQueue<E>
```

E indicates the type of elements held in this queue.

It has and Comparator to maintain the order of the elemnts in the queue.

When you initilize a PriorityQueue you can construct it with the pre-defined Comparator. 

It implemented Queue interface.
