from graphics import *
import math


def drawLine(x0,y0,z0,x1,y1,z1,color):
	ax, ay = x0-(z0*0.3), y0-(z0*0.3)
	bx, by = x1-(z1*0.3), y1-(z1*0.3)
	print(ax,",",ay)
	print(bx,",",by)
	line=Line(Point(ax,ay),Point(bx,by));
	line.setFill(color)
	line.setWidth(3)
	line.draw(win_obj)


def drawSolid(vertex1,vertex2):
	for i in range(c):
		x0 = vertex1[i][0]
		y0 = vertex1[i][1]
		z0 = vertex1[i][2]
		x1 = vertex2[i][0]
		y1 = vertex2[i][1]
		z1 = vertex2[i][2]
		drawLine(x0,y0,z0,x1,y1,z1,"green")

###################

vertex1 = []
f=open("input.txt","r")
c=int(f.readline())		## No. of Edges in the Object 
vertex1=[]					#list for vertex1 of edges
vertex2=[]					#list for vertex2 of edges
for i in range(c):
	number_string=f.readline().split(' ')			#Reading string
	#print(number_string)
	number_Array=[int(i) for i in number_string]		#Array of coordinates [x0,y0,z0,x1,y1,z1]
	point=[]
	point.append(number_Array[0])
	point.append(number_Array[1])
	point.append(number_Array[2])
	vertex1.append(point)
	point=[]
	point.append(number_Array[3])
	point.append(number_Array[4])
	point.append(number_Array[5])
	vertex2.append(point)
	

win_obj=GraphWin("Transformation User Window",900,900) 
win_obj.setBackground("Light blue")
win_obj.setCoords(-300,-300,600,600)
x_axis=Line(Point(0,0),Point(600,0)) 
y_axis=Line(Point(0,0),Point(0,600))
z_axis=Line(Point(0,0),Point(-300,-300))      

x_axis.setOutline("Black")
y_axis.setOutline("Black")
z_axis.setOutline("Black")
x_axis.setArrow('last')
y_axis.setArrow('last')
z_axis.setArrow('last')
x_axis.draw(win_obj)
y_axis.draw(win_obj)
z_axis.draw(win_obj)

info_x=Text(Point(580,-10),"+x axis")
info_x.draw(win_obj)

info_y=Text(Point(-10,580),"+y axis")
info_y.draw(win_obj)
info_ny=Text(Point(-280,-280),"+z axis")
info_ny.draw(win_obj)

origin=Text(Point(-10,-10),"origin")
origin.draw(win_obj)

drawSolid(vertex1,vertex2)

win_obj.getMouse()
win_obj.close()

