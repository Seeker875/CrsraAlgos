#Uses python3
import sys
#import math

def getDist(x,y):
	x1=x[0];x2=y[0];y1=x[1];y2=y[1]
	return ((x1-x2)**2+(y2-y2)**2)**0.5

def getMin(ptsList):
	#get 1 dist of 1st points
	d=getDist(ptsList[0],ptsList[1])

	for i in range(len(ptsList)-1):
		for j in range(i+1,len(ptsList)):
			tempD=getDist(ptsList[i],ptsList[j])
			if tempD<d:
				d=tempD

	return d			

def minimum_distance(x, y):
    
    #sorting and getting 2 lists
    pts=list(zip(x,y))
    pts=sorted(pts,key=lambda x:x[0])
    mid = len(pts)//2
    pts1=pts[0:mid]
    pts2=pts[mid:]


    minD = min(getMin(pts1),getMin(pts2))

    boundX= pts[mid][0]

    yList=[]
    for i in range(1,mid):
    	if pts[mid - i][0] < (boundX-minD):
    		break
    	yList.append(pts[mid-i])
    		
    for i in range(mid+1,len(pts)):
    	if pts[i][0] > (boundX +minD):
    		break
    	yList.append(pts[i])		
    	

    yList=sorted(yList,key =lambda x: x[1])

    i=0
    while i < len(yList):
    	for j in range(i+1,min(i+8,len(yList))):
    		tempD = getDist(yList[i],yList[j])
    		if tempD<minD:
    			minD=tempD
    	i+=1		


    return minD

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))