from collections import deque

class Graph:
	def __init__(self , vertex):
		self.matrix = [[0] * vertex for _ in range(vertex)]
		self.size = vertex
		
	def add_edge(self , src , dest):
		if not (0 < src < self.size+1 and 0 <= dest < self.size+1):
			return print("Invalid Edge" , src)
			
		self.matrix[dest -1][src -1] = 1	
		self.matrix[src-1][dest -1] = 1
	
	def print_matrix(self):
		for row in self.matrix:
			print(" ".join(map(str , row)))
			
	def BFS(self , start):
		if not (1 <= start <= self.size):
			print("Invalid Start" , start)
			return
			
		q = deque([start])
		visited = [False] * self.size
		visited[start - 1] = True
		print(start)
		
		while q:
			front = q.popleft()
			
			printed = False
			
			for index , i in enumerate (self.matrix[front - 1] , start = 1):
				if i == 1 and not visited[index - 1]:
					print(index , end = " ")
					q.append(index) 
					visited[index - 1] = True
					printed = True
					
			if printed:
				print()

#Testing
g = Graph(8)
g.add_edge(0,2)
g.add_edge(1 , 2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3 , 4)
g.add_edge(2 , 4)
g.add_edge(4 , 5)
g.add_edge(5 ,6)
g.add_edge(7 ,6)
g.add_edge(6 , 8)
g.BFS(1)
