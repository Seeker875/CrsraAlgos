#!/usr/bin/python3

import sys, threading
import math

sys.setrecursionlimit(2*10**9) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

#global variables
GLOBALX=-math.inf  
Val=0

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  return True
#need to define result list of this fn
def InOrderTraverse(tree,root):
        #0 is key 1 is left 2 is right child
      if tree[root][1]!= -1:
          InOrderTraverse(tree,root=tree[root][1])
     # print(tree[root][0])
       
      global GLOBALX
     # print(f"globalx is {GLOBALX}")
      if tree[root][0] > GLOBALX:
         # print(f'value assigned is {tree[root][0]}') 
                    
          GLOBALX =tree[root][0] 
         
      else:
       #  print(f"globalx inside else is {GLOBALX}")
         # print(tree[root][0]) 
         global Val 
         Val= -1 
        # print(f'Val is {Val}')
      if tree[root][2]!= -1:
          InOrderTraverse(tree,root=tree[root][2])

def main():
  nodes = int(sys.stdin.readline().strip())
  if nodes <=1:
      print("CORRECT")
      return 0
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  
    
  InOrderTraverse(tree,0)  
  
 # print(Val)
  if Val!=-1:
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
