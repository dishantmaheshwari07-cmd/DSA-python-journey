# 🔗 Singly Linked List Implementation from Scratch

### 📝 Project Description
A complete, custom implementation of a **Singly Linked List data structure** built using Object-Oriented Programming (OOP) in Python. Developed within the first 4 days of starting my DSA journey, this script demonstrates how dynamic nodes link together sequentially using pointer references instead of continuous memory blocks (like arrays).

### 🚀 Key Features Implemented
* **🏗️ Node Blueprint:** Custom `node` class initialized with dynamic data slots and reference variables (`next`).
* **⚡ Head Management:** Structured `sll` (Singly Linked List) controller class tracking the entry point (`head`).
* **➕ Dynamic Insertion Operations:**
  * `at_starting(value)`: Inserts a new node at the absolute front in $O(1)$ time complexity.
  * `at_end(value)`: Traverses the list dynamically to attach elements to the tail node.
  * `at_position(value, position)`: Traverses precisely to inject an item at any specific intermediate index with bounds checking.
* **🗑️ Safe Node Deletion:**
  * `delete(position)`: Standard traversal tracking both the `current` and `previous` node pointers to cleanly decouple target elements from memory and re-link the structure seamlessly. Handles structural adjustments when deleting the head node.
* **🔍 List Traversal Display:** Sequential looping loop (`print_data`) to dump active node configurations to the standard output shell.

### 🛠️ Tech Stack & Concepts Explored
* **Language:** Python 3 (Tested on Pydroid 3 environment)
* **DSA Paradigms:** Node allocation, reference links, memory traversal, position offsets, and linked pointer mutations.
