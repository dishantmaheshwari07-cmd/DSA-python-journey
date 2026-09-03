Deque Using Singly Linked List

📌 Description

This project implements a Double Ended Queue (Deque) using a Singly Linked List in Python.

A Deque allows insertion and deletion from both ends.

FRONT                         REAR
  ↓                             ↓
[10] → [20] → [30] → [40] → None

⚙️ Operations Implemented

- "enqueue_front(value)" — Insert an element at the front
- "enqueue_end(value)" — Insert an element at the rear
- "dequeue_front()" — Delete an element from the front
- "dequeue_end()" — Delete an element from the rear
- "peek()" — View the front element
- "is_empty()" — Check whether the deque is empty
- "length()" — Return the number of elements
- "print_data()" — Display all elements

🧠 Implementation

The deque uses two pointers:

- "front" → points to the first node
- "rear" → points to the last node

For insertion at the rear, the "rear" pointer is directly used, so no traversal is required.

For deletion at the rear, a singly linked list does not have a "prev" pointer, so traversal is required to find the node before "rear".

⏱️ Time Complexity

Operation| Complexity
Enqueue Front| O(1)
Enqueue End| O(1)
Dequeue Front| O(1)
Dequeue End| O(n)
Peek| O(1)
Is Empty| O(1)
Length| O(n)
Print Data| O(n)

🧪 Testing

The implementation was tested with:

- Empty deque
- Single-node deque
- Multiple insertions at front
- Multiple insertions at rear
- Deletion from front
- Deletion from rear
- Alternating front/rear operations
- Deleting until empty
- Reusing the deque after becoming empty
- Different data types
- Duplicate values
- Negative and zero values
- Mixed operations
- Empty operations

All tested operations produced the expected deque state.

💡 Key Learning

The main learning from this implementation was understanding how a Deque can be built on top of a Singly Linked List, and why deleting from the rear is O(n) without a previous pointer.

A Doubly Linked List can make rear deletion O(1) because each node has a "prev" pointer.

🚀 Future Learning

Possible future implementations:

- Deque using Doubly Linked List
- Circular Queue
- Queue using Circular Array
- Combining multiple data structures in a larger project
