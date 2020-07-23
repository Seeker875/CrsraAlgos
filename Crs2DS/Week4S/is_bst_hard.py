#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(2*10**9) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(treeNum,minVal,maxVal):
    ####Check if the key is prsent
    ##this will also retturn correct at last nodes
    if treeNum not in tree.keys():
        return True
    elif tree[treeNum][0]<minVal or tree[treeNum][0] >= maxVal:
        return False
    else:
        leftTree = IsBinarySearchTree(tree[treeNum][1],minVal, tree[treeNum][0]) 
        rightTree = IsBinarySearchTree(tree[treeNum][2], tree[treeNum][0],maxVal)
        return leftTree and rightTree

def main():
  nodes = int(sys.stdin.readline().strip())
 
  minVal=sys.maxsize*-1
  maxVal=sys.maxsize
  global tree
  tree = {}
  for i in range(nodes):

    tree[i]=(list(map(int, sys.stdin.readline().strip().split())))
 # print(tree)
  if IsBinarySearchTree(0,minVal,maxVal):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
