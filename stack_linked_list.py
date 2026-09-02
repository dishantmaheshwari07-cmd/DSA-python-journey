class node:
	def __init__(self , value):
		self.data = value
		self.next = None
		
class stack:
	def __init__(self):
		self.top = None #first element
		
	
	def push(self ,value):			
		new_node = node(value)
		new_node.next = self.top
		self.top = new_node
		
	def pop(self):
		if self.top != None:
			delete_value = self.top.data
			self.top = self.top.next
			return delete_value
		return ("linked list is already empty")
		
	def peek(self):
		if self.top:
			return self.top.data
		return "linked list is empty"
	
	def is_empty(self):
		if self.top:
			return("Not empty")
		return ("empty")
	
	def length(self):
		t1 = self.top
		count = 1
		if self.top:
			while t1.next!= None:
				count+=1
				t1 = t1.next
			return count
		return 0
	
	def print_data(self):
		if self.top:
			t1 = self.top
			while t1.next != None:
				print(t1.data)
				t1 = t1.next
			print(t1.data)
