class node:
	def __init__(self, data , next = None):
		self.data = data
		self.next = next
		
class sll:
	def __init__(self , data):
		self.head = node(data)
		
	def at_end (self , value):
		t1 = self.head
		
		if self.head.next is None:
			t1.next = (node(value))
		else:	
			while t1.next != None:
				t1 = t1.next
			last_node = node(value)
			t1.next = last_node
			
	def print_data(self):
		t1 = self.head
		while t1.next != None:
			print(t1.data)
			t1 = t1.next
		print(t1.data)
		
	def at_starting(self , value):
		self.head = node(value , self.head)
		
	def at_position(self , value , position):
		t1 = self.head
		if position == 1:
			self.at_starting(value)
			
		else:
			check = False
			txn = 1
			b4_position = position - 1
				
			while t1 :
				if txn == b4_position:
					old_next = t1.next
					new_node = node(value , old_next)
					t1.next = new_node
					check = True
					break
				txn += 1
				t1 = t1.next
					
			if not check:
				print("Number is out of range and did not add")
				
	def delete(self , position):
		t1 = self.head
		txn = 1	
		check = False
		
		if position == 1:
			self.head = t1.next
			check = True
		else:
			while t1:
				if txn == position -1:
					previous = t1
					
				if txn == position:
					previous.next = t1.next
					check = True
					break
				else:
					t1 = t1.next
					txn+=1
				
		if not check:
			print("No index found , no change")					
s = sll(10)

s.at_end(20)
s.at_end(30)
s.at_end(40)
s.at_end(50)

print("Original:")
s.print_data()

print("Delete position 1:")
s.delete(1)
s.print_data()

print("Delete position 3:")
s.delete(3)
s.print_data()

print("Delete last position:")
s.delete(3)
s.print_data()

print("Invalid position:")
s.delete(10)
				
