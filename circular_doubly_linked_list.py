class node:
	def  __init__(self ,data , prev = None , next = None):
		self.data = data
		self.prev = prev
		self.next = next

class dll:
	def __init__(self,value):
		self.head = node(value)	
		self.head.next = self.head
		self.head.prev = self.head	
		
	def at_end(self , value):
		if self.head != None:
			t1 = self.head
			
			while t1.next != self.head:
				t1 = t1.next
				
			new_node = node(value , next = self.head)
			t1.next = new_node
			new_node.prev = t1
			self.head.prev = new_node
			
		else:
			self.head = node(value)
			self.head.next = self.head
			self.head.prev = self.head	
	
	def at_start(self , value):
		if self.head is None:
			self.head = node(value)
			self.head.prev = self.head
			self.head.next = self.head
			return
		
		t1= self.head	
		while t1.next != self.head:
			t1 = t1.next
		last = t1	
		new_node = node(value , prev = last)
		new_node.next = self.head
		self.head.prev = new_node
		self.head = new_node
		last.next = self.head
		
	def print_data(self):
		if self.head == None :
			print("No element in linked list")
			return
			
		t1 = self.head 
		while t1.next != self.head:
			t1 = t1.next
		last = t1
		
		print("forward")
		t1 = self.head
		
		while t1.next != self.head :
			print(t1.data)
			t1 = t1.next
		print(t1.data)	
		
		print("Backward")		
		while t1.prev  != last:
			print(t1.data)
			t1 = t1.prev
		print(t1.data)
		
	def at_position(self , value , position):
		if position <= 0:
			print("Enter a index according to 1 base")
			
		else:
			if self.head != None:
				t1 = self.head
				txn = 1
				check_end = 1
				check = False
				
				while t1.next != self.head:
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
						
							if t1.next == self.head:
								break
				
				if not check :
					print("No index found in the range , no updation")
			else:
				print("No element in linked list")
				
	def delete_position(self , position):		
		if self.head != None:
			if position <= 0:
				print("Enter a index according to 1 base")
				
			else:
				t1 = self.head
				txn = 1	
				check = False	
				
				check_end = 1
				while t1.next != self.head :
					check_end+=1
					t1= t1.next
				last = t1
						
				if position == check_end:	
					if self.head.prev != self.head: #checking it is not only element
						check = True
						t1.prev.next = self.head
						self.head.prev = t1.prev
					else:
						self.head = None
					return ("Deleted succesfully")
					
				t1 = self.head
				
				if position == 1:
					check = True
					
					if t1.next != self.head:	
						self.head = t1.next
						self.head.prev = last
						last.next = self.head 			
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
							
							if t1.next == self.head:
								break
							
				if not check:
					return("No index found , not delete anything")
		else:
			return ("Linked list is empty cant delete any thing")
				
