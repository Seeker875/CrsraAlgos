# Uses python3
import sys



def get_majority_element(a,left,right):
    # if left == right:
    #     return -1
    # if left + 1 == right:
    #     return a[left]
    #write your code here
    n=len(a)

    if n==1:
        return a[0]

    mid=n//2
    leftVal= get_majority_element(a[:mid],left,right)   
    rightVal= get_majority_element(a[mid:],left,right)

    if leftVal!= -1:
        count=0
        for i in range(n):
            if a[i] ==leftVal:
                count+=1
        if count>mid:
            return leftVal

    if rightVal!= -1:
        count=0
        for i in range(n):
            if a[i] ==rightVal:
                count+=1
        if count>mid:
            return rightVal        

   
    return -1       


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)