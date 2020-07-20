#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size
GLOBALX=-9999999  
def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  return True
#need to define result list of this fn
def InOrderTraverse(tree,root):
        #0 is key 1 is left 2 is right child
      if tree[root][1]!= -1:
          InOrderTraverse(tree,root=tree[root][1])
      #print(tree[root][0])
       
      global GLOBALX
     # print(f"globalx is {GLOBALX}")
      if tree[root][0] >= GLOBALX:
          #print(tree[root][0]) 
                    
          GLOBALX =tree[root][0] 
         
      else:
          #print(f"globalx inside else is {GLOBALX}")
         # print(tree[root][0]) 
                    

          return -1 

      if tree[root][2]!= -1:
          InOrderTraverse(tree,root=tree[root][2])

def main():
  nodes = int(sys.stdin.readline().strip())
  if nodes ==0:
      print("INCORRECT")
      return 0
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  
  
  
  Val= InOrderTraverse(tree,0)  
  

  if Val!=-1:
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
