# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    #sort segments as per start values
    segments = sorted(segments,key=lambda x: x.start)

    #start with end pt of 1st line
    tempPoint=segments[0].end

    for s in segments:
        # if next points start point lies in1st segment
        if s.start > tempPoint:
            tempPoint = s.end
        #check for if 1 line segment lies in other    
        if s.end < tempPoint:
            tempPoint = s.end   
            # change last point in the points list
            points[-1]= tempPoint 
        # not getting repeated points: 
        if tempPoint not in points:
            points.append(tempPoint)

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
