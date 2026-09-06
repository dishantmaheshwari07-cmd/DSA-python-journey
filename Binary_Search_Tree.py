# Make node
class node:
	def __init__(self, value):
		self.data = value
		self.left = None
		self.right = None


class bst:
	def __init__(self):
		self.root = None

	def insertion(self, value):
		if not self.root:
			self.root = node(value)
			return "Tree created"
		self.found = False
		
		def insert_at_mid(root, value):
			
			if root != None:
				if root.data == value:
					self.found = True
					return root

			if root is None:
				return node(value)

			if root.data > value:
				check = insert_at_mid(root.left, value)
				root.left = check
				return root

			else:
				check = insert_at_mid(root.right, value)
				root.right = check
				return root

		insert_at_mid(self.root, value)
		if not self.found:
			return value
		else:
			return f"{value} already exists"
			
	def searching(self, target):
		if self.root is None:
			return "Tree did not formed"
			
		def search(root , target):
			if root :
				if root.data == target:
					return True
				elif root.data > target:
					return search(root.left , target)
				else:
					return search(root.right ,target)
			else:
				return False
				
		found = search(self.root , target)
		if found:
			print(f"{target} found")
		else:
			print(f"{target} did not found")
			
	def delete(self, target):
		
		if self.root is None:
			return "No tree created"
			
		def search_to_delete(root , target , parent = None):
			if root :
				if root.data == target:
					return [root , parent]
					
				elif root.data > target:
					return search_to_delete(root.left , target , parent = root)
				else:
					return search_to_delete(root.right ,target , parent = root)
			else:
				return None
				
		def del_node(node , go_to, step):
			
			if node is None:
				return 
				
			least_parent = node
			least_node = getattr(node , go_to)
		    
			while getattr(least_node ,step) is not None:
				least_parent = least_node
				least_node = getattr(least_node,step)
		        
			return [least_node , least_parent]
		
		found_node = search_to_delete(self.root , target)

		if not found_node:
			return  f"{target} not found"
		
		node =found_node[0]
		parent = found_node[1]
		
		if node.left == node.right == None:
			if parent.data > node.data:
				parent.left= None
				return parent
			else:
				parent.right = None
				return parent
				
		if node.right:
			go_to = "right"
			step = "left"
			final = del_node(node , go_to, step)	
			
		else:
			go_to = "left"
			step = "right"
			final = del_node(node , go_to, step)	
			
		last_node = final[0]
		last_parent  = final[1]
		node.data = last_node.data
		setattr(last_parent, step, None)

# --- EDGE CASES TEST RUNNER ---

test_tree = bst()

print("=== 1. INSERTION TESTS ===")
print(test_tree.insertion(50))   # Root create hona chahiye
print(test_tree.insertion(30))   # Left child
print(test_tree.insertion(70))   # Right child
print(test_tree.insertion(20))   # Deep left child
print(test_tree.insertion(40))   # Deep right child (30 ke right)
print(test_tree.insertion(35))   # 40 ke left mein (Deep link)

print("\n=== 2. DUPLICATE CHECK ===")
print(test_tree.insertion(30))   # Warning message aana chahiye

print("\n=== 3. SEARCHING CHECKS ===")
test_tree.searching(35)          # Found aana chahiye
test_tree.searching(999)         # Did not found aana chahiye

print("\n=== 4. DELETION CHECKS (The Ultimate Test) ===")

# Test Case A: Ek aisa node delete karna jiska sirf ek subtree ho (20 ka left/right check)
print("Deleting 20 (Node with single or leaf subtree)...")
test_tree.delete(20)
test_tree.searching(20)          # Did not found aana chahiye

# Test Case B: 2 children wala complex deletion (Right ka lowest)
# 30 ke do children hain (humne 20 delete kar diya tha par 40 aur 35 hain)
print("\nDeleting 30 (Node with 2 children - Triggering your getattr logic)...")
test_tree.delete(30)
test_tree.searching(30)          # Did not found aana chahiye
test_tree.searching(35)          # 35 abhi bhi dhoondne par milna chahiye!
