#Uses python3

import sys

def explore(v):
    visited[v]=1
   # print(adj[v])
    for w in adj[v]:
    #    print(f'w outside if is {w}')
        if visited[w]==0:
     #       print(f'w is {w}')
            explore(w)
    return 0

def DFS(adj):
    '''
    Depth First search
    '''
    cc=0
    for i in range(n):
        if visited[i]==0:
            explore(i)
            cc+=1
    return cc        
def number_of_components(adj):
    result = DFS(adj)
    #write your code here
    
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    visited=[0]*n
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
