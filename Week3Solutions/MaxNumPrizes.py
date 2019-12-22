# Uses python3
import sys

def optimal_summands(n):

	#write your code here	
	# for i in range(0,(n//2)+2):
	#   #starting from 1
	#   if mySum+i+1<=n:
	#       summands.append(i+1)
	#       mySum += i+1
	
	half = n//2

	if n<=3:

		if n<=2:
			return [n]

		if n==3:
			half=n

	mySum = half*(half+1)/2

	while mySum>n:
		half-=1
		mySum =  half*(half+1)/2
	
	summands=list(range(1,half+1))

	if mySum<n:
		summands[-1] = summands[-1]+n-int(mySum)
	


	return summands

if __name__ == '__main__':
	input = sys.stdin.read()
	n = int(input)
	summands = optimal_summands(n)
	print(len(summands))
	# for x in summands:
	# 	print(x, end=' ')





