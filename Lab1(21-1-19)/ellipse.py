from graphics import *	
def draw_ellipse(x,y):
	pt=Point(x0+x,y0+y)
	pt.draw(window)
	pt=Point(x0+x,y0-y)
	pt.draw(window)
	pt=Point(x0-x,y0+y)
	pt.draw(window)
	pt=Point(x0-x,y0-y)
	pt.draw(window)
	time.sleep(0.03)
	#print("("+str(x)+","+str(y)+")")

#taking input from user
print("Enter coordinate of center of ellipse:")
x0=int(input("Enter x-coordinate:"))
y0=int(input("Enter y-coordinate:"))
print("Enter length of axes:")
a=int(input("Enter length of major axis:"))
b=int(input("Enter length of minor axis"))

window=GraphWin("2016UCP1103_ELLIPSE",600,600)         #for viewport(device coordinates)

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
msg=Text(Point(x0,y0-10), "C("+str(x0)+","+str(y0)+")")                     #for center of ellipse
msg.draw(window)

x=0
y=b
d1=(b*b)-(a*a*b)+(0.25*a*a)
while((a*a)*(y-0.5)>(b*b)*(x+1)):
	if d1<0:
		d1+=(b*b)*(2*x+3)
	else:
		d1+=(b*b)*(2*x+3)+(a*a)*(-2*y+2)
		y=y-1
	x=x+1
	draw_ellipse(x,y)
d2=(b*b)*(x+0.5)*(x+0.5)+a*a*(y-1)*(y-1)-a*a*b*b
while y>0:
	if d2<0:
		d2+=b*b*(2*x+2)+a*a*(-2*y+3)
		x+=1
	else:
		d2+=a*a*(-2*y+3)
	y-=1
	draw_ellipse(x,y)

window.getMouse()
window.close()
