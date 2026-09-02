# 📚 Stack Implementation Using Linked List (From Scratch)

### 📝 Project Description
A custom, high-performance implementation of a **Stack data structure** built using dynamic Linked List nodes instead of static arrays. This approach guarantees that stack memory allocations grow and shrink dynamically, ensuring optimal resource utilization during runtime operations.

### 🚀 Key Features Implemented
* **🏗️ Node Structure:** A sleek `node` class managing independent data entries and a singular `next` reference.
* **📈 $O(1)$ Push Operation:** Inserts new elements onto the top of the stack efficiently by shifting the `top` reference without traversing the list.
* **📉 $O(1)$ Pop Operation:** Removes and returns the top-most item while automatically garbage-collecting the decoupled node reference. Handles underflow validation smoothly.
* **🔍 Peek & State Checks:** Includes a `peek()` method to view the active top element without removing it, and `is_empty()` for structural state tracking.
* **📊 Dynamic Metrics:** Implements a custom linear traversal loop to calculate the exact `length()` of the stack configurations at any instance.

### 🛠️ Tech Stack & Concepts Explored
* **Language:** Python 3 (Optimized for mobile compilers like Pydroid 3)
* **DSA Paradigms:** Last-In-First-Out (LIFO) execution flow, constant-time reference mutation, boundary state handling, and node parsing loops.
