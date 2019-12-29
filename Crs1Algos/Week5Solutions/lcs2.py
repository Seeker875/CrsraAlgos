#Uses python3

import sys

def lcs2(a, b):
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

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
