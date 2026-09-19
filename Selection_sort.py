#selection sort
data = [100,1,8,5,4,9,7,3,2,6,7,4]

def selection_sort(data):
	if not data:
		return []
		
	for i in range(len(data) -1):
		min_index = i
		for index , j in enumerate(data[i :] , start = i):
			if data[min_index] > j:
				min_index = index
				
		data[i] , data[min_index] = data[min_index] , data[i]

	return data

		
def insertion_sort(data):
	if not data:
		return []
		
	for i in range(1,len(data)):
		key = data[i]
		j = i
		
		#insertion sorting with while loop
		while j > 0:
			if data[j -1] > key:
				data[j] = data[j -1]
			else:
				data[j] = key
				break				
			j -= 1
			
		if j == 0:
			data[0] = key
		
		#insertion sorting with for loop	
#		for j in range(i , 0 , -1):			
#		
#			if data[j - 1] > key:
#				data[j] = data[j -1]		
#			else: # Current element to insert into sorted portion
#				data[j] = key
#				break
#		else:
#			data[0] = key
		
	return data
					
		
print(insertion_sort(data))
