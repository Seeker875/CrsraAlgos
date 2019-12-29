# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)
    
    #since list is sorted
    if a[left] > x or a[right-1] < x:
        return -1
    
    	
    while left < right:
        #print(f'left is {left}')
        mid = (left+right)//2
        #print(f'Mid is {mid}')
        tempVal=a[mid]
        #print(f'tempVal is {tempVal}')
        if tempVal==x:
        		return mid
        elif tempVal>x:
        		right = mid
        else:
        		left= mid+1
    return -1	
			


def linear_search(a, x):
	for i in range(len(a)):
		if a[i] == x:
			return i
	return -1

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n = data[0]
	m = data[n + 1]
	a = data[1 : n + 1]
	for x in data[n + 2:]:
		# replace with the call to binary_search when implemented
		print(binary_search(a, x), end = ' ')