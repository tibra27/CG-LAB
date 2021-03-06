from graphics import *

#function for center of polygon
def getcenter():
        global cx,cy
        for i in range(0,s):
                cx+=pbt[i][0]
                cy+=pbt[i][1]
        cx/=s
        cy/=s
#function for translation
def translation(tx,ty):
	for i in range(0,s):
		pbt[i][0]=int(pbt[i][0]+tx)
		pbt[i][1]=int(pbt[i][1]+ty)
	print(pbt)
#function for scaling
def scaling(sx,sy):
	for i in range(0,s):
		pbt[i][0]=int(pbt[i][0]*sx)
		pbt[i][1]=int(pbt[i][1]*sy)
	print(pbt)

#taking input from user

print("Enter no. of sides in polygon:")
s=int(input("Enter sides:"))
print("Enter the points:")
pbt=[]                
for i in range(0,s):
        print("enter x coordinate of point-",i+1,":")
        x=int(input())
        print("enter y coordinate of point-",i+1,":")
        y=int(input())
        a=[x,y]
        pbt.append(a)
	
	
window=GraphWin("2016UCP1103_SCALING",600,600)           #for viewport(device coordinates)

window.setCoords(-300,-300,300,300)                  #for window(user coordinates)
window.setBackground("yellow")
#drwing user coordinate system
X=Line(Point(-300,0),Point(300,0))              #for drawing X-axis
X.setArrow('both')
X.setOutline('blue')
X.draw(window)
msg=Text(Point(290,10), "+X")                    
msg.draw(window)
msg=Text(Point(-290,10), "-X")                    
msg.draw(window)

Y=Line(Point(0,-300),Point(0,300))              #for drawing Y-axis
Y.setArrow('both')
Y.setOutline('blue')
Y.draw(window)
msg=Text(Point(10,290), "+Y")                    
msg.draw(window)
msg=Text(Point(10,-290), "-Y")                    
msg.draw(window)

msg=Text(Point(0,0), "(0,0)")                     #for origin
msg.draw(window)

#drawing original polygon
for i in range(1,s):
        x1=pbt[i-1][0]
        y1=pbt[i-1][1]
        x2=pbt[i][0]
        y2=pbt[i][1]
        line=Line(Point(x1,y1),Point(x2,y2))
        line.setFill("red")
        line.draw(window)
        Text(Point(x1,y1),"("+str(x1)+","+str(y1)+")").draw(window)
x1=pbt[0][0]
y1=pbt[0][1]
x2=pbt[s-1][0]
y2=pbt[s-1][1]
line=Line(Point(x1,y1),Point(x2,y2))
line.setFill("red")
line.draw(window)
Text(Point(x2,y2),"("+str(x2)+","+str(y2)+")").draw(window)


#calling translation
sx=float(input("Enter Scaling in x:Sx="))
sy=float(input("Enter Scaling in y:Sy="))
cx=0
cy=0
getcenter()
translation(-cx,-cy)
scaling(sx,sy)
translation(cx,cy)


#drawing scaled polygon  
for i in range(1,s):
        x1=pbt[i-1][0]
        y1=pbt[i-1][1]
        x2=pbt[i][0]
        y2=pbt[i][1]
        line=Line(Point(x1,y1),Point(x2,y2))
        line.setFill("blue")
        line.draw(window)
        Text(Point(x1,y1),"("+str(x1)+","+str(y1)+")").draw(window)
x1=pbt[0][0]
y1=pbt[0][1]
x2=pbt[s-1][0]
y2=pbt[s-1][1]
line=Line(Point(x1,y1),Point(x2,y2))
line.setFill("blue")
line.draw(window)
Text(Point(x2,y2),"("+str(x2)+","+str(y2)+")").draw(window)
 
window.getMouse()
window.close()
