# Uses python3
import sys

def getGCD(num1,num2):
    #gcd
   # print(num1)
    #print(num2)
    if num2==0:
        return num1
    elif num1==0:
        return num2 
    elif num1==1:
        return num1         
    elif num1<=num2:
        #num2 is bigger
        # so getting divisor to reduce number of subtractions
        div =num2//num1
        
        return getGCD(num2-(div*num1),num1)
    else:
        div =num1//num2
        return getGCD(num1-(div*num2),num2)        
    

# def lcm_fast(a, b):
    
    
#     Min= min(a,b)
#     Max=max(a,b)
#     if Max%Min==0:
#         return Max
    
#     gcd=getGCD(a,b)
#     print(gcd)
    
    
#     if  gcd == 1:
#         return a*b
    
    
#     for l in range(Max, Max*Min-Max+1,Max):
#         print(l)
#         if l%Min==0:
#             return l



def lcm_fast(a, b):
 
   gcd=getGCD(a,b)
   return((a*b)//gcd)



if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_fast(a, b))

