class Graph:
	def __init__(self , vertex):
		self.matrix = [[0] * vertex for _ in range(vertex)]
		self.size = vertex
		
	def add_edge(self , src , dest):
		if not (0 <= src < self.size+1 and 0 <= dest < self.size+1):
			return "Invalid Edge"
			
		self.matrix[dest -1][src -1] = 1	
		self.matrix[src-1][dest -1] = 1
	
	def print_matrix(self):
		for row in self.matrix:
			print(" ".join(map(str , row)))
			
	def DFS(self , start):
		if not 0 < start < self.size +1:
			return print("Starting not found")
	
		stack = [start]
		visited = [start]
		pointer = start -1	
		while stack:
			found = False
			
			for  index , i  in enumerate(self.matrix[pointer] , start = 1):
				if i == 1 and index not in visited:
					visited.append(index)
					stack.append(index)
					pointer = index - 1
					found = True
					break
						
			if not found:
				stack.pop()
				try :
					pointer = stack[-1] -1
				except IndexError:
					break
		
		for i in visited:
			if i != visited[-1]:
				print(i , end = " -> ")	
			else:
				print(i)
				
#Testing
g = Graph(6)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3 , 4)
g.add_edge(4,6)
g.add_edge(6,5)
g.add_edge(3 , 5)
g.DFS(5)

		
