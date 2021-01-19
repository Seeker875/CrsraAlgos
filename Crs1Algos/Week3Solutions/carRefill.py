# python3
import sys


def compute_min_refills(distance, tank, stops):
    
    n=len(stops)
    
    #### sort just to make sure input is confirmed
    stops.sort()
    #append starting and ending points
    ### insert at 0th position
    stops.insert(0,0)
    stops.append(distance)

    numRefill=0
    currentRefill=0
    while currentRefill<=n:
        ##### lastRefill is needed to keep track of where we last refilled
    	lastRefill = currentRefill
        
        #### stop either if refills needed are more than gas stations
        #### or even with refill you cant reach next destination
        
        ### current refill denotes the position
    	while currentRefill<=n and (stops[currentRefill+1]-stops[lastRefill])<=tank:
    		currentRefill +=1
        
        ### if we can not reach next point 
    	if currentRefill == lastRefill:
    		return -1
        ####increment numRefill, this is in outer while
        #### count if position is not the last and beyond
    	if currentRefill<=n:
    		numRefill+=1

    return numRefill


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
