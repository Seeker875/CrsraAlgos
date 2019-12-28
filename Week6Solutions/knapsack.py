# Uses python3
import sys

def optimal_weight(W, w):
    
  '''
  knapsack, W wt allowed, w vector of wts
  '''
  	#wt matrix

  Val =[[0 for x in range(W+1)] for y in range(len(w)+1)]
    #Check for every number up to wt, use memoization
  for i in range(1,(len(w)+1)):
    	for wt in range(1,(W+1)):
    		#wt above in the matrix
    		Val[i][wt] = Val[i-1][wt]
    		if w[i-1]<=wt:
    			tempVal= Val[i-1][wt-w[i-1]] + w[i-1]# need to change this if value is given
    			if Val[i][wt]< tempVal:
    				Val[i][wt] = tempVal

  return Val[len(w)][W]				


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
