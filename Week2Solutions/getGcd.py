#"python3"

import sys
#O log n
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
    


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(getGCD(a, b))
    #print(b)


# if __name__ == '__main__':
#     a, b = map(int, input().split())
#     print(getGCD(a, b))