import numpy.random as nprnd
from binarytree import Node, show
from collections import deque

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
			self.left.print_preorder()

		if self.right is not None:
			self.right.print_preorder()

	def print_post_order(self):
		if self.left is not None:
			self.left.print_post_order()

		if self.right is not None:
			self.right.print_post_order()

		print self.value

	def is_root(self):
		return self.parent is None

	def is_right_child(self):
		if self.is_root():
			return False 
		return self.value >= self.parent.value

	def is_left_child(self):
		if self.is_root():
			return False 
		return self.value < self.parent.value

	def left_rotate(self):
		if self.is_root() or self.is_left_child():
			return

		pivot = self
		og_left = self.left
		og_parent = self.parent

		og_parent.parent = pivot
		pivot.left = og_parent

		og_parent.right = og_left
		og_left.parent = og_parent
		
		return og_parent

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

	def test_rotate(self):
		if self.root is None or self.root.right is None:
			return

		og_parent = self.root.right.left_rotate()
		
		if og_parent == self.root:
			self.root = og_parent.parent


	def print_level_order(self):
		if self.root is None:
			return

		queue = deque()
		queue.append(self.root)

		while len(queue) != 0:
			current_node = queue.popleft()
			print current_node.value

			if current_node.left is not None:
				queue.append(current_node.left)

			if current_node.right is not None:
				queue.append(current_node.right)

def random_numers(total_numbers):
	return[int(1000 * nprnd.random()) for i in range(total_numbers)]

tree = BST()
a=random_numers(10)

for i in a:
	tree.add(i)

show(tree.root)
tree.test_rotate()
show(tree.root)