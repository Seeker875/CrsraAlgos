# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    
    def InOrderTraverse(start):

      if self.left[start]!= -1:
        InOrderTraverse(start=self.left[start])
      self.result.append(self.key[start])
      if self.right[start] != -1:
          InOrderTraverse(start=self.right[start])


    InOrderTraverse(start=0)
    
    
    return self.result

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    def PreOrderTraverse(start):

      self.result.append(self.key[start])

      if self.left[start]!= -1:
        PreOrderTraverse(start=self.left[start])
      
      if self.right[start] != -1:
          PreOrderTraverse(start=self.right[start])


    PreOrderTraverse(start=0)            
    return self.result

  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    def PostOrderTraverse(start):

      
      
      if self.left[start]!= -1:
        PostOrderTraverse(start=self.left[start])
      
      if self.right[start] != -1:
          PostOrderTraverse(start=self.right[start])
      self.result.append(self.key[start])    

    PostOrderTraverse(start=0)            
    return self.result            
    return self.result

def main():
    tree = TreeOrders()
    tree.read()
    # print(f"keys are {tree.key}")
    # print(f'left are {tree.left}')
    # print(f'right are {tree.right}')
    #print(tree.key)
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
