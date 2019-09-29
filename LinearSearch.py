'''Algorithm:
1. Traverse entire array  
2. Check until number is found 
3. stop

Time Complexity:
Best: O(1) when 1st element is desired
Worst: O(n) when element is the last one or not present'''

def LinearSearch(arr, x):
	'''Functon to run Linear search in an array'''
	for i in range (0,len(arr)):
		if arr[i]==x:
			return i
	return -1

arr = [1,2,3,4,5,6,7,8,9]
x = 6

result = LinearSearch(arr, x)
print ('result', result)
