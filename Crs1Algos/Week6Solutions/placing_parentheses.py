# Uses python3

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

#evaluate all combinations for min and max
#mins can be used in case of 2 -ves
  




def get_maximum_value(dataset):
    d=[]
    op=[]
    for _ in dataset:
        if _.isnumeric():
            d.append(int(_))
        else:
            op.append(_)

    n=len(d)
    M=[[0 for x in range(n)] for y in range(n)]
    m=[[0 for x in range(n)] for y in range(n)]

    for i in range(n):
        M[i][i],m[i][i]=d[i],d[i]

    def MinAndMax(i,j):

        #evaluate all combinations for min and max
        #mins can be used in case of 2 -ves
        MinVal=float("inf")
        MaxVal=-float("inf")

        for k in range(i,j):
            M1=M[i][k]
            M2=M[k+1][j]
            m1=m[i][k]
            m2=m[k+1][j]

            # a=eval(f'{M1} {op[k]} {M2}')
            # b=eval(f'{M1} {op[k]} {m2}')
            # c=eval(f'{m1} {op[k]} {M2}')
            # d=eval(f'{m1} {op[k]} {m2}')

            a=evalt(M1,M2,op[k])
            b=evalt(M1,m2,op[k])
            c=evalt(m1,M2,op[k])
            d=evalt(m1,m2,op[k])

            MinVal = min(MinVal,a,b,c,d)
            MaxVal = max(MaxVal,a,b,c,d)
        return MinVal,MaxVal      

    for s in range(1,n):
        for i in range(0,(n-s)):
            j=i+s
            m[i][j],M[i][j] = MinAndMax(i,j)



    return M[0][n-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
