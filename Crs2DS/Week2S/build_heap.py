# python3


# def build_heap(data):
#     """Build a heap from ``data`` inplace.

#     Returns a sequence of swaps performed by the algorithm.
#     """
#     # The following naive implementation just sorts the given sequence
#     # using selection sort algorithm and saves the resulting sequence
#     # of swaps. This turns the given array into a heap, but in the worst
#     # case gives a quadratic number of swaps.
#     #
#     # TODO: replace by a more efficient implementation
#     swaps = []
#     for i in range(len(data)):
#         for j in range(i + 1, len(data)):
#             if data[i] > data[j]:
#                 swaps.append((i, j))
#                 data[i], data[j] = data[j], data[i]
#     return swaps

def shiftDown(data,idx):
    '''
    input i position as input
    Shifts down an element maintaining heap str
    '''
    size= len(data) -1
    swaps=[]
    while idx<=(size//2):
        minIdx = idx

        # -1 for zero based idx
        leftChild = 2*idx+1
        rightChild = 2*idx+2
        #print(f'leftChild  {leftChild}') # 
       
        #
        if  leftChild <= size and data[leftChild]<data[minIdx]:
            minIdx = leftChild

        if  rightChild <= size and data[rightChild]<data[minIdx]:
            minIdx= rightChild

        if  minIdx !=idx:
            tempVal = data[minIdx]
            data[minIdx] = data[idx]
            data[idx] = tempVal
            #swaps.append(shiftDown(data,minIdx))
            #swaps.append(*shiftDown(data,minIdx))
            swaps.append((idx,minIdx))
            idx=minIdx
        else:
            break;
            

    return swaps    



def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    swapsMain=[]
    size= len(data)
    ## -1 to check for left child only when tree is not complete
    # example size 5 
    for i in range((size//2)-1,-1,-1):
        #print(f'sDown idx {i}')
        swaps=shiftDown(data,i)
        for sTuple in swaps:
            swapsMain.append(sTuple)

    return swapsMain    


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    #print(swaps)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
