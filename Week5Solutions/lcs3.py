#Uses python3

import sys

def longestSequence(a, b):
    sLen,tLen=len(a),len(b)

    DistM = [[0 for x in range(tLen+1)] for y in range(sLen+1)] 


    for j in range(1,(tLen+1)): 
        for i in range(1,(sLen+1)): 
            Ins= DistM[i][j-1]
            Del= DistM[i-1][j]
            Mtch= DistM[i-1][j-1]
            
            if a[i-1]==b[j-1]:
                DistM[i][j]=Mtch+1
              
            else:
                DistM[i][j]=max(Ins,Del)

    lcs=''
    i=sLen
    j=tLen
    while i>0 and j>0:
            
            if a[i-1]== b[j-1]:
                
                lcs+=str(a[i-1])
               
                i-=1
                j-=1
            elif DistM[i-1][j] > DistM[i][j-1]: 
                i-=1
            else: 
                j-=1
                    
 
    return lcs[::-1]  

def lcs3(a, b, c):
    #Getting longest sequence of a and b
    a = longestSequence(a, b)

    sLen,tLen=len(a),len(b)

    DistM = [[0 for x in range(tLen+1)] for y in range(sLen+1)] 


    for j in range(1,(tLen+1)): 
        for i in range(1,(sLen+1)): 
            Ins= DistM[i][j-1]
            Del= DistM[i-1][j]
            Mtch= DistM[i-1][j-1]
            
            if a[i-1]==b[j-1]:
                DistM[i][j]=Mtch+1
              
            else:
                DistM[i][j]=max(Ins,Del)

    return DistM[sLen][tLen] 

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))