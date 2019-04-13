# python3
import sys


def compute_min_refills(distance, tank, stops):
    
    n=len(stops)

    stops.sort()
    #append starting and ending points
    stops.insert(0,0)
    stops.append(distance)

    numRefill=0
    currentRefill=0
    while currentRefill<=n:
    	lastRefill = currentRefill

    	while currentRefill<=n and (stops[currentRefill+1]-stops[lastRefill])<=tank:
    		currentRefill +=1
    	if currentRefill == lastRefill:
    		return -1
    	if currentRefill<=n:
    		numRefill+=1

    return numRefill


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))