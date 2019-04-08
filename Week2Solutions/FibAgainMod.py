#python3

import sys
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


def FibonacciMod(fibN,n):
    
    if n<=3:
        if(n==3):
            pisano=8
        elif(n==2):
            pisano=3    
        #changed this part
        else:
            pisano=60

    else:
        remList=[]
        #getting pisano by count
        upperBound=6*n+2
        for i in range(0,upperBound):
            remList.append(FibonacciFastList(i)%n)
            if i >2 and remList[i-1]==0 and remList[i]==1 :
                pisano=i-1
                break
    
    rem = fibN % pisano
    
    return FibonacciFastList(rem) % n
  



if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(FibonacciMod(a, b))