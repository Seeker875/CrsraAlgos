# Uses python3
import sys

def get_change(m):
    #m is moey
    coins=[1,3,4]
    MinNumcoins=[0]*(m+1)

    for denom in range(1,m+1):
    	MinNumcoins[denom]=float('inf')

    	for i in range(len(coins)):
    		if coins[i]<=m:
    			numCoins=MinNumcoins[denom-coins[i]]+1
    			if MinNumcoins[denom]>numCoins:
    				MinNumcoins[denom]= numCoins

    return MinNumcoins[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
