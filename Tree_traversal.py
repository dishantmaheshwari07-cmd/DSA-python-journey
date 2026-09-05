class node:
	def __init__(self, value):
		self.data = value
		self.left = self.right = None
		
class Binary_Tree:
	def __init__(self):
		self.root = None
		
	def find_node(self ,root , parent):
		if root.data == parent:
			return root
			
		if root.left:
			left_tree = self.find_node (root.left , parent)
			if left_tree:
				return left_tree
		if root.right:
			right_tree = self.find_node (root.right , parent)
			if right_tree:
				return right_tree
			else :
				return None
				
	def add_element(self , value ,  parent = None):
		
		if not self.root :
			self.root = node(value)
			return "Tree created"
		
		if not parent:
			return "Enter the parent name"
					
		parent_node = self.find_node (self.root,parent)
		if not parent_node:
			return "No parent found"
			
		if not parent_node.left:
			parent_node.left = node(value)
			return f"{value} added to {parent}"
		elif not parent_node.right:
			parent_node.right = node(value)
			return f"{value} added to {parent}"
		else:
			return f"Alredy 2 child are there in {parent}"
	
	def pre_order(self):
		if not self.root:
			return "tree is empty"		
		
		num = []
		def preorder_sequence(root):
			if root == None:
				return 
			num.append(root.data)
			preorder_sequence(root.left)
			preorder_sequence(root.right)		
		
		preorder_sequence(self.root)
		return num
		
	def inorder(self):
		if not self.root:
			return "tree is empty"		
		
		num = []
		def inorder_sequence(root):
			if root == None:
				return 
				
			inorder_sequence(root.left)
			num.append(root.data)
			inorder_sequence(root.right)
		
		inorder_sequence(self.root)
		return num
		
	def post_order(self):
		if not self.root:
			return "tree is empty"		
		
		num = []
		def postorder_sequence(root):
			if root == None:
				return 
			postorder_sequence(root.left)
			postorder_sequence(root.right)
			num.append(root.data)
		
		postorder_sequence(self.root)
		return num
					
tree = Binary_Tree()

tree.add_element(10)
tree.add_element(5, 10)
tree.add_element(20, 10)
tree.add_element(3, 5)
tree.add_element(7, 5)
tree.add_element(15, 20)
tree.add_element(25, 20)
tree.add_element(6, 7)

print("Postorder:", tree.post_order())
