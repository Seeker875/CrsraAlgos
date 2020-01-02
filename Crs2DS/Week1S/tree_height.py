# python3

import sys
import threading


def compute_height(n, parents):
    
    
    myTree={}
    for i in range(0,n):
        myTree[i] =[]
    
    
    for i in range(0,n):
        #print(i)
        
        if  parents[i]==-1:
            root = i
        else:
            myTree[parents[i]].append(i)

    def Height(node):
        
        if myTree[node] == []:
            return 0
        #return 1 + max(Height(myTree[node][0]),Height(myTree[node][1]))  
        return 1 + max([Height(x) for x in myTree[node]])      

    
    return Height(root)+1     
    

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


#compute_height(5, [-1,0,4,0,3 ])
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
