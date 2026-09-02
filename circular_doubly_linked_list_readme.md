# 🔄 Circular Doubly Linked List (CDLL) Implementation from Scratch

### 📝 Project Description
An advanced implementation of a **Circular Doubly Linked List (CDLL)** using Object-Oriented Programming (OOP) in Python. This data structure eliminates null pointers by connecting the tail node back to the head node (and vice versa), forming a continuous bidirectional loop in memory.

### 🚀 Key Features Implemented
* **🏗️ Circular Pointer Ring:** Initializes nodes where the head's `next` and `prev` pointers loop back to itself, avoiding any `None` references.
* **↔️ Bidirectional Loop Traversal:** The `print_data()` method showcases full circular traversal, printing forward from head-to-tail and shifting into a backward loop smoothly.
* **➕ Circular Edge Insertion:**
  * `at_start(value)`: Inserts at the front and re-routes the tail's `next` pointer to preserve the circular ring in $O(N)$ time.
  * `at_end(value)`: Appends nodes to the tail while continuously anchoring the final `next` link back to the head node.
  * `at_position(value, position)`: Traverses using step-counters to safely split inner links and inject elements.
* **🗑️ Safe Ring Deletion:**
  * `delete_position(position)`: Handles boundary rewires when deleting single-node rings, head updates, and includes a live command prompt confirmation check (`Y/N`).

### 🛠️ Tech Stack & Concepts Explored
* **Language:** Python 3 (Optimized for Pydroid 3 mobile workspace)
* **DSA Paradigms:** Circular data mapping, multi-pointer configuration, memory rings, bounds validation, and interactive execution routines.
