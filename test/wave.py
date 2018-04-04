import rhinoscriptsyntax as rs
import math

sources=[[50,50,0],[50,0,0],[0,0,0]]
count=[100,100]
points=[]
for j in range (count[1]):
    for i in range (count[0]):
        x=i
        y=j
        zTemp=0
        sum=0
        for source in sources:
            dist=rs.Distance(source,[x,y,zTemp])
            sum=sum+math.sin(dist)
        z=sum
        points.append( [x,y,z] )
rs.AddSrfPtGrid (count,points)