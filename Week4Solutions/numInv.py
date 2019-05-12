# Uses python3
import sys


# def Merge(b,c):
#     d=[]
#     while len(b)>0 and len(c)>0:
#         if b[0] <= c[0]:
#             d.append(b[0])
#             b.remove(b[0])

#         else:
#             d.append(c[0])
#             c.remove(c[0])
			
#     d=d+b+c
#     return d        



# def MergeSort(unSort):
#     n=len(unSort)

#     if n ==1:
#         return unSort

#     mid =n//2
#     b =  MergeSort(unSort[:mid])
#     c = MergeSort(unSort[mid:])

#     a = Merge(b,c)

#     return a      

def Merge(b,c):
	d=[]
	count=0
	while len(b)>0 and len(c)>0:
		if b[0] <= c[0]:
			d.append(b[0])
			b.remove(b[0])

		else:
			d.append(c[0])
			c.remove(c[0])
			count+=1
	count+=count		
	d=d+b+c
	return d,count        



def MergeSort(unSort):
	n=len(unSort)

	if n ==1:
		return unSort
	count=0
	mid =n//2
	b =  MergeSort(unSort[:mid])
	c = MergeSort(unSort[mid:])

	a,tempCount = Merge(b,c)
	count+=tempCount
	return a,count   

def get_number_of_inversions(a, b, left, right):
	number_of_inversions = 0
	if right - left <= 1:
		return number_of_inversions
	#ave = (left + right) // 2
	ave = len(a)//2
	number_of_inversions += get_number_of_inversions(a, b, left, ave)
	number_of_inversions += get_number_of_inversions(a, b, ave, right)
	#write your code here
	a, tempCount = MergeSort(a[:ave], a[ave:])
	number_of_inversions += tempCount

	return number_of_inversions

if __name__ == '__main__':
	input = sys.stdin.read()
	n, *a = list(map(int, input.split()))
	b = n * [0]
	print(get_number_of_inversions(a, b, 0, len(a)))


