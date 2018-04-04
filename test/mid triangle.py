import rhinoscriptsyntax as rs 

def subd(pol,ratio):
	pts = rs.PolylineVertices(pol)

	vec = rs.VectorCreate(pts[2],pts[1])
	vec = rs.VectorScale(vec,ratio)

	midPt = rs.VectorAdd(pts[1],vec)

	pts1 = [pts[0],pts[1],midPt,pts[0]]
	pts2 = [pts[0],midPt,pts[2],pts[0]]

	triangle1 = rs.AddPolyline(pts1)
	triangle2 = rs.AddPolyline(pts2)
	#subd(triangle1,ratio)
	#subd(triangle2,ratio)


triangle = rs.GetObject("please click on a triangle",rs.filter.curve)
ratio    = rs.GetReal("please type the ratio of the subdivision",0.5)
subd(triangle,ratio)

