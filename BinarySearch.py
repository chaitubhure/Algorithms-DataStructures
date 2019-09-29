'''Algorithm:
1. Sort array in ascending order (Prereq) and if right-most>=left-most
2. Half the number of elements in array  (L + (R-L)/2) 
3. Check mid element is equal to desired
4. If not, and if mid element is greater than desired element
5. Repeat entire process in lower subarray (0 to mid-1)
6. Else repeat entire process in upper subarray (mid+1 to n)

Time Complexity:
Best: O(1) when mid element is desired
Worst: O(logn) '''

def BinarySearch(arr,l,r,x):
	'''Function to perform Binary search
	This algorithm requires array to be sorted in
	ascending order'''
	if r>=l:
		mid=l+(r-l)//2
		if arr[mid]==x:
			return mid
		elif arr[mid]<=x:
			return BinarySearch(arr,mid+1,r,x)
		else:
			return BinarySearch(arr,l,mid-1,x)

arr = [10,20,30,40,50,60,70,80,90]
x = 70

result = BinarySearch(arr,0,len(arr)-1,x)
print('result', result)
