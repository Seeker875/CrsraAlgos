#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 18:31:50 2019

@author: Taranpreet singh
"""

def lcm_fast(a, b):
    Min= min(a,b)
    Max=max(a,b)
    for l in range(1, Min + 1,Max):
        print(l)
        
        if l % Min== 0:
            return l

    return a*b

lcm_fast(5,8)

#min(5,8)

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        #print(l)
        if l % a == 0 and l % b == 0:
            return l

    return a*b


fibList=[0,1]

def FibonacciFastLast(n):

	if n<=1:
		return n
	else:
		listLen=len(fibList)	

		if n>(listLen-1):
			for i in range(listLen,n+1):
				fibList.append((fibList[i-1]+fibList[i-2])%10)

		return fibList[n]

FibonacciFastLast(327305)



fibList=[0,1]

def FibonacciFastList(n):

	if n<=1:
		return n
	else:
		listLen=len(fibList)	

		if n>(listLen-1):
			for i in range(listLen,n+1):
				fibList.append(fibList[i-1]+fibList[i-2])

		return fibList[n]	
        
        
print(FibonacciFastList(150))

for i in range(0,30):
    print(fibList[i]%5)

#Pisano periods
#If n = F (2k) (k ≥ 2), then π(n) = 4k;
# if n = F (2k + 1) (k ≥ 2), then π(n) = 8k + 4. 

#
    
#  
    
def FibonacciMod(fibN,m):
    
    if m<=3:
        if(m==3):
            pisano=8
        elif(m==2):
            pisano=3
        else:
            pisano=1
    elif m%2==0:
        pisano = 2*m
    else:
        pisano = 4*(m-1) + 4 
    print(pisano)
    print("rem")
    rem = fibN % pisano
    print(rem)
    print(FibonacciFastList(rem))
    return FibonacciFastList(rem) % m
    

        
FibonacciMod(2015,3)
FibonacciMod(239,1000)   
FibonacciMod(2816213588,239) 

 
FibonacciMod(10,2) 
 
for i in range(4,30):
    print(i)
    print(FibonacciMod(i,5) ) 



def lcm_fast(a, b):
    
    
    Min= min(a,b)
    Max=max(a,b)
    if Max%Min==0:
        return Max
    
    gcd=getGCD(a,b)
    print(gcd)
    
    
    if  gcd == 1:
        return a*b
    
    
    for l in range(Max, Max*Min-Max+1,Max):
        print(l)
        if l%Min==0:
            return l


lcm_fast(2000000000,1999999999)

lcm_fast(6,8)


lcm_fast(28851538,1183019)
#1933053046
lcm_fast(5,11)



def lcm_fast(a, b):
 
   gcd=getGCD(a,b)
   return((a*b)//gcd)


#If m and n are coprime, then π(mn) is the least common multiple of π(m) and π(n), 
#by the Chinese remainder theorem. For example, π(3) = 8 and π(4) = 6 imply π(12) = 24.
# Thus the study of Pisano periods may be reduced to that of Pisano periods of 
#prime powers q = pk, for k ≥ 1.

def getPisano(m):
    if m<=3:
        if(m==3):
            pisano=8
        elif(m==2):
            pisano=3
        else:
            pisano=1
    elif m%2==0:
        pisano = 2*m
    else:
        pisano = 4*(m-1) + 4 
    return pisano

 
for i in range(0,30):
    print(f'{i}------{getPisano(i)}')



def getPisano(n):
    if n<=3:
        if(n==3):
            pisano=8
        elif(n==2):
            pisano=3
        else:
            pisano=1

    else:
        remList=[]
        #getting pisano by count
        upperBound=6*n+2
        for i in range(0,upperBound):
            remList.append(FibonacciFastList(i)%n)
            if i >2 and remList[i-1]==0 and remList[i]==1 :
                pisano=i-1
                break
    return pisano


getPisano(5)

remList=[]
        #getting pisano by count
n=10     
upperBound=6*n+2
for i in range(0,upperBound):
            remList.append(FibonacciFastList(i)%n)
            if i >2 and remList[i-1]==0 and remList[i]==1 :
                pisano=i-1
                break

for i in range(0,30):
    print(f'{i}------{getPisano(i)}')
    
    
    

    
fibListLast=[0,1]

def FibonacciFastLast(n):

    if n<=1:
        return n
    else:
        m=n%60
        listLen=len(fibListLast)	

        if n>(listLen-1):
            for i in range(listLen,60):
                fibListLast.append((fibListLast[i-1]+fibListLast[i-2])%10)

        return fibListLast[m]

FibonacciFastLast(161)




def getFibSumDiff(n1,n2):

    Max= max(n1,n2)
    Min=min(n1,n2)
    #print(f'{Max} and {Min}')
    #print(f'{FibonacciFastList(Max+2)} and {FibonacciFastList(Min+1)}')
    #return abs((FibonacciFastLast(Max+2)-1) - (FibonacciFastLast(Min+1)-1))
    fibL=FibonacciFastLast(Max+2)-1
    fibS=FibonacciFastLast(Min+1)-1
    if fibL<fibS:
        fibL=10 +fibL
    return fibL - fibS
        
    
getFibSumDiff(10,200)