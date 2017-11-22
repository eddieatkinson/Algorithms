import numpy.random as nprnd
from binarytree import Node, show

class MyBinaryTreeNode(Node):
	def __init__(self, value):
		self.value = value
		self.parent = None
		self.left = None
		self.right = None

	def add(self, new_node):
		if new_node.value >= self.value:
			if self.right is None:
				self.right = new_node
				new_node.parent = self
			else:
				self.right.add(new_node)
		else:
			if self.left is None:
				self.left = new_node
				new_node.parent = self
			else:
				self.left.add(new_node)

	def exists(self, value_to_search_for):
		if self.value == value_to_search_for:
			return True
		elif self.value < value_to_search_for:
			if self.right is not None:
				return self.right.exists(value_to_search_for)
			else:
				return False
		else:
			if self.left is not None:
				return self.left.exists(value_to_search_for)
			else:
				return False

class BST:
	def __init__(self):
		self.root = None

	def add(self, value):
		new_node = MyBinaryTreeNode(value)

		if self.root is None:
			self.root = new_node
		else:
			self.root.add(new_node)

	def exists(self, value):
		if self.root is None:
			return False
		else:
			return self.root.exists(value)

def random_numers(total_numbers):
	return[int(1000 * nprnd.random()) for i in range(total_numbers)]

tree = BST()
a=random_numers(10)

for i in a:
	tree.add(i)

show(tree.root)
print tree.exists(a[9])