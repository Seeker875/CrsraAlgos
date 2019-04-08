#python3

#Memoization for Fibonacci
# list for shell
fibList=[0,1]

def FibonacciFastList(n):

	if n<=1:
		return n
	else:
		listLen=len(fibList)	

		if n>(listLen-1):
			for i in range(listLen,n+1):
				fibList.append(fibList[i-1]+fibList[i-2])

		return fibList[n]	

n = int(input())
print(FibonacciFastList(n))