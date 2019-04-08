#python3
#import sys
    
fibListLast=[0,1]

def FibonacciFastLast(n):

    if n<=1:
        return n
    else:
        m=n%60
        listLen=len(fibListLast)	

        if n>(listLen-1):
            for i in range(listLen,60):
                fibListLast.append((fibListLast[i-1]+fibListLast[i-2])%10)

        return fibListLast[m]



def getFibSum(n):

	num=FibonacciFastLast(n+2)
	if num==0:
		num = 10

	return  num -1


n = int(input())
print(getFibSum(n))		






