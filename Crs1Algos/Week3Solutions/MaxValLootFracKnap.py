#python3

import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    
    #get ratio
    vw=[values[i]/weights[i] for i in range(0,len(values))]
    #get idx of the sorted list
    ### need idx to get element from wt as well
    vwIdx= sorted(range(len(vw)),key=vw.__getitem__,reverse=True)

    for idx in vwIdx:
        #### this makes it fractional
        #### we are taking minimum as well
    	a=min(weights[idx],capacity)
        
        #### reduce the capacity
    	capacity-=a
    	value+= a*values[idx]/weights[idx]

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
