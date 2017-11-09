class MyQueue:
	def __init__(self):
		self.queue = []

	def enqueue(self, new_element):
		# Adds the new element to the end of the array.
		self.queue.append(new_element)
		pass

	def dequeue(self):
		# Removes the first element from the array.
		element = self.queue[0]
		del self.queue[0]
		return element

class MyStack:
	def __init__(self):
		self.stack = []

	def push(self, new_element):
		# Add the new element to the top of the stack.
		self.stack.append(new_element)
		pass

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

my_stack = MyStack()

my_stack.push(3)
my_stack.push(4)
my_stack.push(5)

print my_stack.stack

print my_stack.pop()

# print my_stack.stack

print my_stack.peek()

my_queue = MyQueue()

my_queue.enqueue(1)
my_queue.enqueue(2)

print my_queue.queue

print my_queue.dequeue()
# print my_queue.queue
