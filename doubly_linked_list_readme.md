# 🔗 Doubly Linked List (DLL) Implementation from Scratch

### 📝 Project Description
A comprehensive implementation of a **Doubly Linked List (DLL) data structure** using Object-Oriented Programming (OOP) in Python. This project demonstrates bidirectional data navigation by maintaining two pointer references (`prev` and `next`) inside each individual element node, allowing for efficient forward and backward list traversals.

### 🚀 Key Features Implemented
* **🏗️ Bidirectional Node Blueprint:** A custom `node` class built with dual pointers (`prev` and `next`) alongside the standard `data` field.
* **↔️ Dual-Direction Traversal:** The `print_data()` method showcases complete list printing from head-to-tail (Forward) and immediately loops back from tail-to-head (Backward) using structural references.
* **➕ Dynamic Node Insertion:**
  * `at_start(value)`: Inserts a new node at the absolute front in $O(1)$ time complexity.
  * `at_end(value)`: Iterates sequentially to dynamic tail nodes to attach new components.
  * `at_position(value, position)`: Maps 1-based bounds to insert values anywhere seamlessly between existing link layers.
* **🗑️ Interactive Node Deletion:**
  * `delete_position(position)`: Standard boundary deletions for structural safety. Includes an interactive console verification step (`Y/N`) before finalizing intermediate node deletions.

### 🛠️ Tech Stack & Concepts Explored
* **Language:** Python 3 (Tested on Pydroid 3 environment)
* **DSA Paradigms:** Bidirectional referencing, structural re-linking, memory graph manipulation, element counting, and data persistence safeguards.
