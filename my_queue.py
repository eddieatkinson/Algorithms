class MyQueue:
	def __init__(self):
		self.stack1 = MyStack()
		self.stack2 = MyStack()

	def enqueue(self, new_element):
		# Adds the new element to the end of the array.
		if self.stack2.peek() is None:
			self.stack1.push(new_element)
		else:
			while self.stack2.peek() is not None:
				self.stack1.push(self.stack2.pop())
			self.stack1.push(new_element)

	def dequeue(self):
		# Removes the first element from the array and return it.
		if self.stack2.peek() is None:
			while self.stack1.peek() is not None:
				self.stack2.push(self.stack1.pop())
		return self.stack2.pop()

class MyStack:
	def __init__(self):
		self.stack = []

	def push(self, new_element):
		# Add the new element to the top of the stack.
		self.stack.append(new_element)

	def pop(self):
		# Remove the top most element and also return it.
		last_index = len(self.stack) - 1
		element = self.stack[last_index]
		del self.stack[last_index]
		return element

	def peek(self):
		# Return the top most element.
		last_index = len(self.stack) - 1
		return self.stack[last_index]