"""
line tree
"""

import rhinoscriptsyntax as rs

def main():
    
    startLine = rs.GetObject("Clikc and select a line to get start the recursive tree")
    angle  = rs.GetReal ("Type the angle for the brunch", 30)
    branch(startLine,angle)
    newLines= branch(startLine,angle)


def branch (line,ang):
    
    startPt = rs.CurveStartPoint(line)
    endPt   = rs.CurveEndPoint(line)
    vec     = rs.VectorCreate(endPt,startPt)
    vec1    = rs.VectorRotate (vec,ang,[0,0,1])
    vec2    = rs.VectorRotate (vec,-ang,[0,0,1]) 
    
    endPt1  = rs.PointAdd(endPt,vec1)
    endPt2  = rs.PointAdd(endPt,vec2)
    
    line1   = rs.AddLine(endPt,endPt1)
    line2   = rs.AddLine(endPt,endPt2)
    return (line1,line2)
main()
