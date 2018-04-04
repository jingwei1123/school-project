import rhinoscriptsyntax as rs
import math

for i in range(100):
    x=i/10
    y=math.cos(i/20)
    z=math.sin(i/10)
    rs.AddPoint([x,y,z])