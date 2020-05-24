class MyCircularDeque:

	def __init__(self, k: int):
		self.queue = [0] * (k + 1)
		self.length = k + 1
		self.head = 0
		self.tail = 0

	def move_forward(self, pos):
		return (pos + 1) % self.length

	def move_backward(self, pos):
		return (pos - 1) % self.length

	def insertFront(self, value):
		if not self.isFull():
			self.queue[self.head] = value
			self.head = self.move_backward(self.head)
			return True
		else:
			return False

	def insertLast(self, value):
		if not self.isFull():
			self.tail = self.move_forward(self.tail)
			self.queue[self.tail] = value
			return True
		else:
			return False

	def deleteFront(self):
		if not self.isEmpty():
			self.head = self.move_forward(self.head)
			return True
		else:
			return False

	def deleteLast(self):
		if not self.isEmpty():
			self.tail = self.move_backward(self.tail)
			return True
		else:
			return False

	def getFront(self):
		if not self.isEmpty():
			return self.queue[self.move_forward(self
				.head)]
		else:
			return -1

	def getRear(self):
		if not self.isEmpty():
			return self.queue[self.tail]
		else:
			return -1

	def isEmpty(self):
		if self.head == self.tail:
			return True
		else:
			return False

	def isFull(self):
		if self.move_forward(self.tail) == self.head:
			return True
		else:
			return False