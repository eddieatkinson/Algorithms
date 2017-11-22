class MyTreeNode:
	def __init__(self, value):
		self.value = value
		self.parent = None
		self.children = []

	def add_child(self, child_node):
		self.children.append(child_node)
		child_node.parent = self

	def remove_child(self, child_node):
		del self.children[self.children.indexof(child_node)]

root = MyTreeNode(5)
root.add_child(MyTreeNode(10))
root.add_child(MyTreeNode(20))

for child in root.children:
	print child.value