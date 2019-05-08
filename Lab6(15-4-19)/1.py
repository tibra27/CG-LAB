from graphics import *
import math

f=open("input.txt","r")
c=int(f.readline())
vertex1 = []
f=open("input.txt","r")
c=int(f.readline())
vertex1=[]
vertex2=[]
for i in range(c):
	number_string=f.readline().split(' ')
	number_Array=[int(i) for i in number_string]
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
	

win_obj=GraphWin("PROJECTION_1103",900,900) 
win_obj.setBackground("Light blue")
win_obj.setCoords(-300,-300,600,600)
x_axis=Line(Point(-300,0),Point(600,0)) 
y_axis=Line(Point(0,-300),Point(0,600))
z_axis=Line(Point(300,300),Point(-300,-300))      

x_axis.setOutline("Black")
y_axis.setOutline("Black")
z_axis.setOutline("Black")
x_axis.setArrow('both')
y_axis.setArrow('both')
z_axis.setArrow('both')
x_axis.draw(win_obj)
y_axis.draw(win_obj)
z_axis.draw(win_obj)

info_x=Text(Point(580,-10),"+x axis")
info_x.draw(win_obj)
info_x=Text(Point(-280,-10),"-x axis")
info_x.draw(win_obj)
info_y=Text(Point(-10,580),"+y axis")
info_y.draw(win_obj)
info_y=Text(Point(-10,-280),"-y axis")
info_y.draw(win_obj)
info_ny=Text(Point(-280,-280),"+z axis")
info_ny.draw(win_obj)
info_ny=Text(Point(280,280),"-z axis")
info_ny.draw(win_obj)
origin=Text(Point(-10,-10),"origin")
origin.draw(win_obj)

def drawLine(x0,y0,z0,x1,y1,z1,color):
	ax, ay = x0-(z0*0.3), y0-(z0*0.3)
	bx, by = x1-(z1*0.3), y1-(z1*0.3)
	#print(ax,",",ay)
	#print(bx,",",by)
	line=Line(Point(ax,ay),Point(bx,by));
	line.setFill(color)
	line.setWidth(3)
	line.draw(win_obj)


def drawSolid(vertex1,vertex2,color):
	for i in range(c):
		x0 = vertex1[i][0]
		y0 = vertex1[i][1]
		z0 = vertex1[i][2]
		x1 = vertex2[i][0]
		y1 = vertex2[i][1]
		z1 = vertex2[i][2]
		drawLine(x0,y0,z0,x1,y1,z1,color)

drawSolid(vertex1,vertex2,"green")


tx=int(input("Enter Tx to translate:"))
ty=int(input("Enter Ty to translate:"))
tz=int(input("Enter Tz to translate:"))
vertex3=[]
vertex4=[]
for i in range(c):
	point=[]
	x0 = vertex1[i][0]+tx
	point.append(x0)
	y0 = vertex1[i][1]+ty
	point.append(y0)
	z0 = vertex1[i][2]+tz
	point.append(z0)
	vertex3.append(point)
	point=[]
	x1 = vertex2[i][0]+tx
	point.append(x1)
	y1 = vertex2[i][1]+ty
	point.append(y1)
	z1 = vertex2[i][2]+tz
	point.append(z1)
	vertex4.append(point)
	
drawSolid(vertex3,vertex4,"red")


vertex1=vertex3
vertex2=vertex4
vertex3=[]
vertex4=[]
print("Choose principle plane:: 1>XY  2>YZ  3>XZ")
f=int(input())

if f==1:
	a1=1
	b1=1
	c1=0
elif f==2:
	a1=0
	b1=1
	c1=1
elif f==3:
	a1=1
	b1=0
	c1=1

for i in range(c):
	point=[]
	x0 = vertex1[i][0]*a1
	point.append(x0)
	y0 = vertex1[i][1]*b1
	point.append(y0)
	z0 = vertex1[i][2]*c1
	point.append(z0)
	vertex3.append(point)
	point=[]
	x1 = vertex2[i][0]*a1
	point.append(x1)
	y1 = vertex2[i][1]*b1
	point.append(y1)
	z1 = vertex2[i][2]*c1
	point.append(z1)
	vertex4.append(point)
print(vertex3)	
drawSolid(vertex3,vertex4,"yellow")
	
	
win_obj.getMouse()
win_obj.close()

