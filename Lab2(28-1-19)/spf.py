from graphics import *
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
		pt=Point(x,y)
		time.sleep(0.03)
		pt.draw(window)
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
		pt=Point(x,y)
		time.sleep(0.03)
		pt.draw(window)
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
	
	msg =Text(Point(x0,y0),"("+str(x0)+","+str(y0)+")")  
	msg.draw(window)
	msg =Text(Point(x1,y1),"("+str(x1)+","+str(y1)+")")
	msg.draw(window)

#fuction for scanline polygon filling
def spf(et,n):
    ycur=500
    aet=[]
    for i in range(len(et)):
        if ycur>et[i][1]:
            ycur=et[i][1]
    while len(et)!=0 or len(aet)!=0:
        p=-1
        cnty=0
        for i in range(len(et)):
            if et[i][1]==ycur:
                cnty+=1
        for i in range(0,cnty):
            for j in range(len(et)):
                if et[j][1]==ycur:
                    break
            aet.append(et[j])
            del et[j:j+1]
        #print(p)
        aet.sort()
        cnt=0
        for i in range(len(aet)):
            if aet[i][3]==ycur:
                cnt+=1
        for i in range(0,cnt):
            for j in range(len(aet)):
                if aet[j][3]==ycur:
                    break
            del aet[j:j+1]
        check=True
        for i in range(len(aet)-1):
            xfrom=aet[i][0]
            xto=aet[i+1][0]
            #print("(",xfrom,xto,")")
            if check==True:
                j=xfrom
                while j<xto:
                    window.plot(j,ycur,"red")
                    j+=1
                check=False
            else:
                check=True
        ycur+=1
        for i in range(len(aet)):
            aet[i][0]+=aet[i][4]
        #print(et,end='\n')
        #print(aet,end='\n')


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
	
	
window=GraphWin("2016UCP1103_POLYGON",600,600)           #for viewport(device coordinates)

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

edge_t=[]                                    #edge table
for i in range(1,s):
        x1=po[i-1][0]
        y1=po[i-1][1]
        x2=po[i][0]
        y2=po[i][1]
        if y2-y1!=0:
            if y1>y2:
                y1,y2=y2,y1
                x1,x2=x2,x1
            m=(x2-x1)/(y2-y1)
            edge_t.append([x1,y1,x2,y2,m])
        draw_line(x1,y1,x2,y2)
x1=po[0][0]
y1=po[0][1]
x2=po[s-1][0]
y2=po[s-1][1]
if y2-y1!=0:
    if y1>y2:
        y1,y2=y2,y1
        x1,x2=x2,x1
    m=(x2-x1)/(y2-y1)
    edge_t.append([x1,y1,x2,y2,m])
draw_line(x1,y1,x2,y2)
spf(edge_t,s)
window.getMouse()
window.close()


