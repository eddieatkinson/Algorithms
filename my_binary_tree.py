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

	def height(self):
		if self.left is None and self.right is None:
			return 1

		left_subtree_height = 0
		right_subtree_height = 0

		if self.left is not None:
			left_subtree_height = self.left.height()

		if self.right is not None:
			right_subtree_height = self.right.height()

		if left_subtree_height > right_subtree_height:
			return left_subtree_height + 1
		else:
			return right_subtree_height + 1

	def print_in_order(self):
		if self.left is not None:
			self.left.print_in_order()
		print self.value

		if self.right is not None:
			self.right.print_in_order()

	def print_preorder(self):
        print self.value

        if self.left is not None:
            self.left.print_in_order()

        if self.right is not None:
            self.right.print_in_order()

    def print_post_order(self):
        if self.left is not None:
            self.left.print_in_order()

        if self.right is not None:
            self.right.print_in_order()

        print self.value

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

	def height(self):
		if self.root is not None:
			return self.root.height()
		return 0

	def print_in_order(self):
		if self.root is not None:
			self.root.print_in_order()


def random_numers(total_numbers):
	return[int(1000 * nprnd.random()) for i in range(total_numbers)]

tree = BST()
a=random_numers(10)

for i in a:
	tree.add(i)

show(tree.root)
# print tree.exists(a[9])
# print tree.height()
tree.print_in_order()