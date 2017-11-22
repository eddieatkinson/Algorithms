class LinkedListNode:
	def __init__(self, value):
		self.value = value
		self.right = None
		self.left = None

	def search(self, value):
		if self.value == value:
			return self

		if self.right is None:
			return None

		return self.right.search(value)

class LinkedList:
	def __init__(self):
		self.start = None
		self.end = None

	def append(self, value):
		new_node = LinkedListNode(value)

		if self.start is None:
			self.start = new_node
			self.end = new_node
		else:
			self.end.right = new_node
			new_node.left = self.end
			self.end = new_node

	def search(self, value):
		if self.start is None:
			return None

		self.start.search(value)

	def print_all_node_values(self):
		current_node = self.start

		while current_node is not None:
			print current_node.value
			current_node = current_node.right

	def remove_last_node(self):
		if self.is_empty():
			return
		elif self.has_only_one_node():
			self.start = None
			self.end = None
		else:
			self.end.left = None
			self.end = self.end.left
			self.end.right = None

	def is_empty(self):
		if self.start is None:
			return True
		else:
			return False

	def has_only_one_node(self):
		if not self.is_empty() and self.start == self.end:
			return True
		else:
			return False

	def delete_at_index(self, target_index):
		current_index = 0
		current_node = self.start

		while current_index != target_index:
			if current_node is None:
				return None
			current_node = current_node.right
			current_index += 1

		if self.end == current_node:
			self.remove_last_node()

		else:
			current_node.right.left = current_node.left
			current_node.left.right = current_node.right
			current_node.right = None
			current_node.left = None





ll = LinkedList()
ll.append(10)
ll.append(11)
ll.append(16)

ll.print_all_node_values()

ll.delete_at_index(1)

ll.print_all_node_values()