class node:
	def __init__(self,value):
		self.data = value
		self.next = None
		
class queue:
	def __init__(self):
		self.front = None
		self.rear = None
		
	def enqueue_front(self , value):
		if not self.front:
			self.front = node(value)
			self.rear = self.front
			
		else:
			new_node = node(value)
			new_node.next = self.front
			self.front = new_node
			
	def enqueue_end(self, value):
		if not self.front:
			self.front = node(value)
			self.rear = self.front
			
		else:
			new_node = node(value)
			self.rear.next = new_node
			self.rear = new_node
	
	def dequeue_front(self):
		if not self.front:
			return 'linked list is empty'
			
		if self.front == self.rear:
			self.front = None
			self.rear =  None
			return ("Dequeue completed")
			
		self.front = self.front.next
		return "dequeue completed"
		
	def dequeue_end(self):
		if not self.front:
			return 'linked list is empty'
			
		if self.front == self.rear:
			self.front = None
			self.rear =  None
			return ("Dequeue completed")
					
		t1 = self.front
		while t1.next != self.rear:
			t1 = t1.next
			
		t1.next = None
		self.rear = t1
		
	def peek(self):
		if self.front:
			return self.front.data
		return "linked list is empty"
		
	def is_empty(self):	
		if self.front:
			return "Not empty"
		return "Empty"
		
	def length(self):
		if not self.front:
			return 0
			
		t1 = self.front
		count = 1
		while t1.next!= None:
			count += 1
			t1= t1.next
		return count
	
	def print_data(self):
		if not self.front:
			return "linked list is empty"
	
		t1 = self.front
		while t1.next != None:
			print(t1.data)
			t1 = t1.next
		print(t1.data)
		
#checking given by chatgpt
q = queue()

# ========== TEST 1: EMPTY DEQUE ==========
print("\n========== TEST 1: EMPTY DEQUE ==========")
print("Length:", q.length())
print("Empty:", q.is_empty())
print("Peek:", q.peek())
print("Delete front:", q.dequeue_front())
print("Delete end:", q.dequeue_end())


# ========== TEST 2: INSERT FRONT INTO EMPTY ==========
print("\n========== TEST 2: INSERT FRONT INTO EMPTY ==========")
q.enqueue_front(10)

print("Length:", q.length())
print("Front:", q.front.data)
print("Rear:", q.rear.data)
print("Peek:", q.peek())

print("Display:")
q.print_data()


# ========== TEST 3: INSERT FRONT MULTIPLE ==========
print("\n========== TEST 3: INSERT FRONT MULTIPLE ==========")
q.enqueue_front(20)
q.enqueue_front(30)

print("Expected: 30 20 10")
print("Actual:")
q.print_data()

print("Front:", q.front.data)
print("Rear:", q.rear.data)
print("Length:", q.length())


# ========== TEST 4: INSERT END ==========
print("\n========== TEST 4: INSERT END ==========")
q.enqueue_end(40)
q.enqueue_end(50)

print("Expected: 30 20 10 40 50")
print("Actual:")
q.print_data()

print("Front:", q.front.data)
print("Rear:", q.rear.data)
print("Length:", q.length())


# ========== TEST 5: DELETE FRONT ==========
print("\n========== TEST 5: DELETE FRONT ==========")
print("Delete:", q.dequeue_front())

print("Expected after delete: 20 10 40 50")
print("Actual:")
q.print_data()

print("Front:", q.front.data)
print("Rear:", q.rear.data)
print("Length:", q.length())


# ========== TEST 6: DELETE END ==========
print("\n========== TEST 6: DELETE END ==========")
print("Delete:", q.dequeue_end())

print("Expected after delete: 20 10 40")
print("Actual:")
q.print_data()

print("Front:", q.front.data)
print("Rear:", q.rear.data)
print("Length:", q.length())


# ========== TEST 7: ALTERNATING FRONT/END ==========
print("\n========== TEST 7: ALTERNATING FRONT/END ==========")

q.enqueue_front(5)
q.enqueue_end(60)
q.dequeue_front()
q.dequeue_end()

print("Expected: 20 10 40")
print("Actual:")
q.print_data()

print("Front:", q.front.data)
print("Rear:", q.rear.data)


# ========== TEST 8: DELETE UNTIL EMPTY ==========
print("\n========== TEST 8: DELETE UNTIL EMPTY ==========")

print("Delete front:", q.dequeue_front())
print("Delete end:", q.dequeue_end())
print("Delete front:", q.dequeue_front())

print("Length:", q.length())
print("Empty:", q.is_empty())
print("Front:", q.front)
print("Rear:", q.rear)


# ========== TEST 9: SINGLE NODE AGAIN ==========
print("\n========== TEST 9: SINGLE NODE AGAIN ==========")

q.enqueue_end(100)

print("Front:", q.front.data)
print("Rear:", q.rear.data)
print("Length:", q.length())

print("Delete end:", q.dequeue_end())

print("Front:", q.front)
print("Rear:", q.rear)
print("Length:", q.length())
print("Empty:", q.is_empty())


# ========== TEST 10: SINGLE NODE FRONT DELETE ==========
print("\n========== TEST 10: SINGLE NODE FRONT DELETE ==========")

q.enqueue_front(200)

print("Front:", q.front.data)
print("Rear:", q.rear.data)

print("Delete front:", q.dequeue_front())

print("Front:", q.front)
print("Rear:", q.rear)
print("Empty:", q.is_empty())


# ========== TEST 11: DIFFERENT DATA TYPES ==========
print("\n========== TEST 11: DIFFERENT DATA TYPES ==========")

q.enqueue_front("hello")
q.enqueue_end(3.14)
q.enqueue_front(True)
q.enqueue_end(-10)

print("Display:")
q.print_data()

print("Length:", q.length())
print("Front:", q.front.data)
print("Rear:", q.rear.data)


# ========== TEST 12: DUPLICATE VALUES ==========
print("\n========== TEST 12: DUPLICATE VALUES ==========")

q = queue()

q.enqueue_front(10)
q.enqueue_end(20)
q.enqueue_front(20)
q.enqueue_end(10)

print("Expected: 20 10 20 10")
print("Actual:")
q.print_data()

print("Length:", q.length())


# ========== TEST 13: NEGATIVE + ZERO ==========
print("\n========== TEST 13: NEGATIVE + ZERO ==========")

q = queue()

q.enqueue_front(0)
q.enqueue_end(-10)
q.enqueue_front(-20)
q.enqueue_end(30)

print("Expected: -20 0 -10 30")
print("Actual:")
q.print_data()

print("Front:", q.front.data)
print("Rear:", q.rear.data)


# ========== TEST 14: MIXED OPERATIONS ==========
print("\n========== TEST 14: MIXED OPERATIONS ==========")

q = queue()

q.enqueue_front(10)
q.enqueue_end(20)
q.enqueue_front(5)
q.enqueue_end(30)

print("Initial:")
q.print_data()

q.dequeue_front()
q.dequeue_end()
q.enqueue_front(1)
q.enqueue_end(40)

print("Expected: 1 10 20 40")
print("Actual:")
q.print_data()

print("Front:", q.front.data)
print("Rear:", q.rear.data)
print("Length:", q.length())


# ========== TEST 15: EMPTY OPERATIONS AGAIN ==========
print("\n========== TEST 15: EMPTY OPERATIONS AGAIN ==========")

while q.front:
    q.dequeue_front()

print("Length:", q.length())
print("Empty:", q.is_empty())
print("Front:", q.front)
print("Rear:", q.rear)
print("Delete front:", q.dequeue_front())
print("Delete end:", q.dequeue_end())
print("Peek:", q.peek())


print("\n[Deque Testing Finished]")
