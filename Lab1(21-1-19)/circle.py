from graphics import *	
def draw_circle(x,y):
	pt=Point(x0+x,y0+y)
	pt.draw(window)
	pt=Point(x0+x,y0-y)
	pt.draw(window)
	pt=Point(x0-x,y0+y)
	pt.draw(window)
	pt=Point(x0-x,y0-y)
	pt.draw(window)
	pt=Point(x0+y,y0+x)
	pt.draw(window)
	pt=Point(x0-y,y0+x)
	pt.draw(window)
	pt=Point(x0+y,y0-x)
	pt.draw(window)
	pt=Point(x0-y,y0-x)
	pt.draw(window)
	time.sleep(0.03)
	#print("("+str(x)+","+str(y)+")")

#taking input from user
print("Enter coordinates of the center:")
x0=int(input("Enter X0:"))
y0=int(input("Enter Y0:"))
R=int(input("Enter radius of Circle:"))

window=GraphWin("2016UCP1103_CIRCLE",600,600)         #for viewport(device coordinates)

window.setCoords(-300,-300,300,300)                  #for window(user coordinates)
window.setBackground("yellow")
#drwing user coordinate system
x_axis=Line(Point(-300,0),Point(300,0))              #for drawing X-axis
x_axis.setArrow('both')
x_axis.setOutline('blue')
x_axis.draw(window)
msg=Text(Point(290,10), "+X")                    
msg.draw(window)
msg=Text(Point(-290,10), "-X")                    
msg.draw(window)

y_axis=Line(Point(0,-300),Point(0,300))              #for drawing Y-axis
y_axis.setArrow('both')
y_axis.setOutline('blue')
y_axis.draw(window)
msg=Text(Point(10,290), "+Y")                    
msg.draw(window)
msg=Text(Point(10,-290), "-Y")                    
msg.draw(window)

msg=Text(Point(10,-10), "O")                         #for origin
msg.draw(window)

center=Point(x0,y0)
center.draw(window)
msg=Text(Point(x0,y0), "C("+str(x0)+","+str(y0)+")")                     #for center of circle
msg.draw(window)

pt=Point(x0+R,y0)
pt.draw(window)	
msg=Text(Point(x0+R+20,y0), "R="+str(R))                 
msg.draw(window)

pt=Point(0,0)
pt.draw(window)
d=1-R                                  #initial d
x=0.0
y=R+0.0
while(y>x):
	x=x+1
	if(d<=0):
		d=d+2*x+3                    #de=2x+3
	else:
		y=y-1
		d=d+2*(x-y)+5                #dse=2(x-y)+5
	draw_circle(x,y)
window.getMouse()
window.close()
