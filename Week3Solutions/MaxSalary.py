#Uses python3

import sys

def isGrtrOrEql(n1,n2):
	num1=str(n1)+str(n2)
	num2=str(n2)+str(n1)

	if int(num1)>=int(num2):
		return True
	else:
		return False	

def largest_number(a):
    #write your code here
    res = ""
    
    while len(a)>0:
    	maxDigit=0
    	for x in a:
        	if isGrtrOrEql(x,maxDigit):
        		maxDigit = x
    	res += str(maxDigit)
    	a.remove(maxDigit)    	
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
