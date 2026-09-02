class node:
	def  __init__(self ,data , prev = None , next = None):
		self.data = data
		self.prev = prev
		self.next = next

class dll:
	def __init__(self,value):
		self.head = node(value)		
		
	def at_end(self , value):
		if self.head != None:
			t1 = self.head
			
			while t1.next != None:
				t1 = t1.next
				
			new_node = node(value)
			t1.next = new_node
			new_node.prev = t1
		else:
			self.head = node(value)
	
	def at_start(self , value):
		if self.head is None:
			self.head = node(value)
			return
			
		new_node = node(value)
		new_node.next = self.head
		self.head.prev = new_node
		self.head = new_node
		
	def print_data(self):
		if self.head == None:
			print("No element in linked list")
			return
			
		t1 = self.head 
		print("forward")
			
		while True:
			print(t1.data)
				
			if t1.next != None:
				t1 = t1.next
			else:
				break
			
		print("Backward")		
			
		while t1:
			print(t1.data)
			t1 = t1.prev		
	
	def at_position(self , value , position):
		if position <= 0:
			print("Enter a index according to 1 base")
			
		else:
			if self.head != None:
				t1 = self.head
				txn = 1
				check_end = 0
				check = False
				while t1:
					check_end += 1
					t1 = t1.next
				t1 = self.head
					
				if position == 1:
					self.at_start(value)
					check = True
					
				elif position == check_end +1 :
					self.at_end(value)
					check = True
					
				else:			
					while True:
						if txn == position -1:
							previous = t1
							new_node = node(value)
							after = previous.next
							
							#connection btw new and previous
							previous.next = new_node
							new_node.prev =previous
							
							#connection btw new and after			
							new_node.next = after
							after.prev = new_node
							check = True
							break
						else:
							txn += 1
							t1 = t1.next
						
							if not t1.next :
								break
				
				if not check :
					print("No index found in the range , no updation")
			else:
				print("No element in linked list")
	
	def delete_position(self , position):
		 
		if position <= 0:
			print("Enter a index according to 1 base")
			
		else:
			t1 = self.head
			txn = 1	
			check = False	
			
			check_end = 0
			while t1:
				check_end+=1
				
				if  t1.next:
					t1 = t1.next
				else:
					break
					
			if position == check_end:	
				if t1.prev != None:
					check = True
					t1.prev.next = None
				else:
					self.head = None
				return ("Deleted succesfully")
				
			t1 = self.head
			
			if position == 1:
				check = True
				if t1.next != None:	
					self.head = t1.next
					self.head.prev = None				
				else:
					self.head = None
				return ("Deleted succesfully")
			
			else:
				while True:
					if txn == position - 1:
						previous = t1
						delete = t1.next
						after = delete.next
						check = True
						
						print(f" Data : {delete.data} ")
						confirm = input("Y/N : ")
						
						if confirm.lower() == "y":
							previous.next = after
							after.prev = previous
							return ("Deleted succesfully")
						else:
							return ("Not deleted")
					else:
						txn += 1
						t1 = t1.next
						if t1 is None:
							break
						
			if not check:
				return("No index found , not delete anything")
				
