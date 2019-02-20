from graphics import *
points=[]                #2-d list for storing border and filled points
for i in range(-300,301):
	points.append([])
	for j in range(-300,301):
		points[i+300].append(" ")
def draw_slope_less(x0,y0,x1,y1):           #for line having slope between -1 and 1
	dy=y1-y0
	dx=x1-x0
	yi=1
	if(dy<0):                               #if slope is between -1 and 0
		yi=-1
		dy=-dy
	dne=2*(dy-dx)
	de=2*dy
	d=2*dy-dx
	y=y0
	r=1
	if x1<x0:
		r=-1
	for x in range(x0,x1,r):
		pt=Point(x+300,y+300)
		time.sleep(0.03)
		pt.draw(window)
		points[x+300][y+300]="bc"#store border point while drawing polygon
		if(d>0):
			y=y+yi
			d=d+dne
		else:
			d=d+de
		#print("("+str(x)+","+str(y)+")")
def draw_slope_more(x0,y0,x1,y1):              #for line having slope greater than 1 or less than -1
	dy=y1-y0
	dx=x1-x0
	xi=1
	if(dx<0):                                  #if slope is less than -1
		xi=-1
		dx=-dx
	dne=2*(dx-dy)
	de=2*dx
	d=2*dx-dy
	x=x0
	r=1
	if y1<y0:
		r=-1
	for y in range(y0,y1,r):
		pt=Point(x+300,y+300)
		time.sleep(0.03)
		pt.draw(window)
		points[x+300][y+300]="bc"#store border point while drawing polygon
		if(d>0):
			x=x+xi
			d=d+dne
		else:
			d=d+de
		#print("("+str(x)+","+str(y)+")")
		
def draw_line(x0,y0,x1,y1):
	if abs(y1-y0) < abs(x1-x0):              #if |slope|<1
		if x0>=x1:                             
			draw_slope_less(x1,y1,x0,y0)             #here we interchange starting and end point of line because we have to draw from bottom to top
		else:
			draw_slope_less(x0,y0,x1,y1)
	else:                                    #if |slope|>1
		if y0>=y1:
			draw_slope_more(x1,y1,x0,y0)
		else:
			draw_slope_more(x0,y0,x1,y1)
	p1=Point(x0+300,y0+300)
	points[x0+300][y0+300]="bc"
	p1.draw(window)
	p2=Point(x1+300,y1+300)
	points[x1+300][y1+300]="bc"
	p2.draw(window)
	msg =Text(Point(x0+300,y0+300),"("+str(x0)+","+str(y0)+")")  
	msg.draw(window)
	msg =Text(Point(x1+300,y1+300),"("+str(x1)+","+str(y1)+")")
	msg.draw(window)

def flood_fill():
	print("Click anywhere inside the polgon to fill it::\n")
	seed_point=(window.getMouse())
	lis=[]
	lis.append(seed_point)
	fc="fc"  #fill color
	bc="bc"  #boundary color
	while(len(lis)!=0):
		pt=lis[len(lis)-1]
		lis.pop()
		x=int(pt.getX())  #accessing x coordinate of point
		y=int(pt.getY())  #accessing y coordinate of point
		if(points[x][y]!=fc and points[x][y]!=bc):
			window.plot(x,y,"red")
			points[x][y]=fc
			pt=Point(x+1,y)
			if(points[x+1][y]!=bc and points[x+1][y]!=fc):
				lis.append(pt)
			pt=Point(x,y+1)
			if(points[x][y+1]!=bc and points[x][y+1]!=fc):
				lis.append(pt)
			pt=Point(x-1,y)
			if(points[x-1][y]!=bc and points[x-1][y]!=fc):
				lis.append(pt)
			pt=Point(x,y-1)
			if(points[x][y-1]!=bc and points[x][y-1]!=fc):
				lis.append(pt)
	
#taking input from user

print("Enter no. of sides in polygon:")
s=int(input("Enter sides:"))
print("Enter the points:")
po=[]
for i in range(0,s):
        print("enter x coordinate of point-",i+1,":")
        x=int(input())
        print("enter y coordinate of point-",i+1,":")
        y=int(input())
        a=[x,y]
        po.append(a)
	
	
window=GraphWin("2016UCP1103_FILLING1",600,600)           #for viewport(device coordinates)

window.setCoords(0,0,600,600)                  #for window(user coordinates)
window.setBackground("white")
#drwing user coordinate system
X=Line(Point(0,300),Point(600,300))              #for drawing X-axis
X.setArrow('both')
X.setOutline('blue')
X.draw(window)
msg=Text(Point(590,310), "+X")                    
msg.draw(window)
msg=Text(Point(10,310), "-X")                    
msg.draw(window)

Y=Line(Point(300,0),Point(300,600))              #for drawing Y-axis
Y.setArrow('both')
Y.setOutline('blue')
Y.draw(window)
msg=Text(Point(310,590), "+Y")                    
msg.draw(window)
msg=Text(Point(310,10), "-Y")                    
msg.draw(window)

msg=Text(Point(300,300), "(0,0)")                     #for origin
msg.draw(window)


for i in range(1,s):
        x1=po[i-1][0]
        y1=po[i-1][1]
        x2=po[i][0]
        y2=po[i][1]
        draw_line(x1,y1,x2,y2)
x1=po[0][0]
y1=po[0][1]
x2=po[s-1][0]
y2=po[s-1][1]
draw_line(x1,y1,x2,y2)
flood_fill()
window.getMouse()
window.close()
