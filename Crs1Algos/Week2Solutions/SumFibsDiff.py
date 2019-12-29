#python3
import sys

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



def getFibSumDiff(n1,n2):

	Max= max(n1,n2)
	Min = min(n1,n2)
	fibL=FibonacciFastLast(Max+2)-1
	fibS=FibonacciFastLast(Min+1)-1
	if fibL<fibS:
		fibL=10 +fibL
	return fibL - fibS



if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(getFibSumDiff(a, b))	


