data = [1,42,8,74,3,84,86,96,3,0,3,7,8]

#def sorting(data):
#	b = 1
#	
#	for index , a in enumerate(data):		
#		for i in range(b):
#			if a > data[i]:
#				data[index] , data[i] = data[i] , data[index]
#		b += 1
#	return data
	
def sorting(data , last = 0):
	
	if not data:
		return ("Empty List ")
		
	if last == len(data) -1:
		return data

	b = 1
	for index , a in enumerate(data):
		if b == len(data):
			return sorting(data , last = last + 1)
		
		if a > data[b]:
			data[index] , data[b] = data[b] , data[index]
		b+=1

# 1. Already sorted
print(sorting([1, 2, 3, 4, 5]))

# 2. Reverse sorted
print(sorting([5, 4, 3, 2, 1]))

# 3. All same values
print(sorting([7, 7, 7, 7, 7]))

# 4. Single element
print(sorting([42]))

# 5. Empty list
print(sorting([]))

# 6. Negative numbers
print(sorting([-5, 3, -1, 0, -10, 8]))

# 7. Duplicates
print(sorting([4, 2, 4, 1, 2, 4, 1]))

# 8. Mixed positive, negative and zero
print(sorting([0, -3, 7, -1, 5, 0, -8, 2]))

# 9. Two elements
print(sorting([2, 1]))

# 10. Two equal elements
print(sorting([5, 5]))


	
			
