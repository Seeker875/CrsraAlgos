#python3

#Fib with list

# fibTabLastD={}

# def FibonacciLastD(n):

# 	#to handle Recursion limit error
# 	if n>2000:
# 		FibonacciLastD(n-2000)

# 	if n <= 1:
# 		return n

# 	else:
# 		if n not in fibTabLastD.keys():
# 			fibTabLastD[n]=FibonacciLastD(n-1)+FibonacciLastD(n-2)
# 		return fibTabLastD[n]%10	



fibList=[0,1]

def FibonacciFastLast(n):

	if n<=1:
		return n
	else:
		listLen=len(fibList)	

		if n>(listLen-1):
			for i in range(listLen,n+1):
				fibList.append((fibList[i-1]+fibList[i-2])%10)

		return fibList[n]



n = int(input())
print(FibonacciFastLast(n))		
