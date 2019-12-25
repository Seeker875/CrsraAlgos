# Uses python3
import sys


'''
Perfect Shortest Path Dp example
1. recursion to memoiszation
2. Guessing, Try all keep the best 1
DAG

'''
def optimal_sequence(n):

    MinOps=[0]*(n+1)
    MinOps[0] = 0
    MinOps[1] = 0   

    getLastOp =[0]*(n+1)

    for num in range(2,n+1):

        MinOps[num] = MinOps[num-1] +1
        getLastOp[num]= 1

        if num%3 == 0:
            temp = MinOps[num//3]+1
            if temp < MinOps[num]:
                MinOps[num]= temp
                getLastOp[num]= 3

        if num%2 == 0:
            temp = MinOps[num//2]+1
            if temp < MinOps[num]:
                MinOps[num]= temp  
                getLastOp[num]= 2

    result=[n]
    fac=n
    while fac != 1:
        if getLastOp[fac]==3:
            fac=fac//3
            result.append(fac)

        elif getLastOp[fac]==2:
            fac=fac//2
            result.append(fac)  
        else:
            fac=fac-1
            result.append(fac)   

    fin=[*reversed(result)]
    #fin.append(MinOps[n])         
    return fin       

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    sequence = optimal_sequence(n)
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
