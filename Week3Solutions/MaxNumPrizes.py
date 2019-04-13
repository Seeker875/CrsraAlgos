# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    mySum=0
    
    for i in range(1,n+1):
    	#starting from 1
    	if mySum+i<=n:
    		summands.append(i)
    		mySum += i

    #getting last value for remaining bal		
    if mySum < n:
    	summands[-1] = summands[-1]+ n -sum(summands)

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
