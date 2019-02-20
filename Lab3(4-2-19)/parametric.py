from graphics import *
def draw_slope_less(x0,y0,x1,y1,color):           #for line having slope between -1 and 1
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
                #time.sleep(0.03)
                pt=Point(x,y)
                pt.setOutline(color)
                pt.draw(window)
                #window.plot(x,y,color)
                #window.plot(x,y,color)
                if(d>0):
                        y=y+yi
                        d=d+dne
                else:
                        d=d+de
                #print("("+str(x)+","+str(y)+")")
def draw_slope_more(x0,y0,x1,y1,color):              #for line having slope greater than 1 or less than -1
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
                #time.sleep(0.03)
                pt=Point(x,y)
                pt.setOutline(color)
                pt.draw(window)
                #window.plot(x,y,color)
                #window.plot(x,y,color)
                if(d>0):
                        x=x+xi
                        d=d+dne
                else:
                        d=d+de
                #print("("+str(x)+","+str(y)+")")
                
def draw_line(x0,y0,x1,y1,color):
        if abs(y1-y0) < abs(x1-x0):              #if |slope|<1
                if x0>=x1:                             
                        draw_slope_less(x1,y1,x0,y0,color)             #here we interchange starting and end point of line because we have to draw from bottom to top
                else:
                        draw_slope_less(x0,y0,x1,y1,color)
        else:                                    #if |slope|>1
                if y0>=y1:
                        draw_slope_more(x1,y1,x0,y0,color)
                else:
                        draw_slope_more(x0,y0,x1,y1,color)


#function for parametric line clipping

def parametricClip(a0,b0,a1,b1):
        n_left=[-1,0]
        n_right=[1,0]
        n_top=[0,1]
        n_bottom=[0,-1]
        te=0.0
        tl=1.0
        d=[a1-a0,b1-b0]
        ndl=n_left[0]*d[0]
        f1=0
        if a1!=a0:
                t_left=-1*(-1*(a0-x_min))/(-1*(a1-a0))
                f1=1
        if ndl<0 and f1==1:
                te=max(t_left,te)
        elif ndl>=0 and f1==1:
                tl=min(t_left,tl)
        ndr=n_right[0]*d[0]
        f2=0
        if a1!=a0:
                t_right=-1*(a0-x_max)/(a1-a0)
                f2=1
        if ndr<0 and f2==1:
                te=max(t_right,te)
        elif ndr>=0 and f2==1:
                tl=min(t_right,tl)
        ndb=n_bottom[1]*d[1]
        f3=0
        if b1!=b0:
                t_bottom=-1*(-1*(b0-y_min))/(-1*(b1-b0))
                f3=1
        if ndb<0 and f3==1:
                te=max(t_bottom,te)
        elif ndb>=0 and f3==1:
                tl=min(t_bottom,tl)
        ndt=n_top[1]*d[1]
        f4=0
        if b1!=b0:
                t_top=-1*(b0-y_max)/(b1-b0)
                f4=1
        if ndt<0 and f4==1:
                te=max(t_top,te)
        elif ndt>=0 and f4==1:
                tl=min(t_top,tl)
        
        x1=a0+(a1-a0)*te
        y1=b0+(b1-b0)*te
        x2=a0+(a1-a0)*tl
        y2=b0+(b1-b0)*tl
        draw_line(int(x1),int(y1),int(x2),int(y2),"red")

#taking input 
print("Enter diagonal points of rectangle:")
x_min=int(input("Enter x_min:"))
y_min=int(input("Enter y_min:"))
x_max=int(input("Enter x_max:"))
y_max=int(input("Enter y_max:"))
print("Enter starting and ending points of line:")
a0=int(input("Enter x0:"))
b0=int(input("Enter y0:"))
a1=int(input("Enter x1:"))
b1=int(input("Enter y1:"))
po=[]
po.append([x_min,y_min])
po.append([x_max,y_min])
po.append([x_max,y_max])
po.append([x_min,y_max])
        
window=GraphWin("2016UCP1103_CLIPPING-2",600,600)           #for viewport(device coordinates)

window.setCoords(-300,-300,300,300)                  #for window(user coordinates)
window.setBackground("white")
#drwing user coordinate system
X=Line(Point(-300,0),Point(300,0))              #for drawing X-axis
X.setArrow('both')
X.setOutline('Black')
X.draw(window)
msg=Text(Point(290,10), "+X")                    
msg.draw(window)
msg=Text(Point(-290,10), "-X")                    
msg.draw(window)

Y=Line(Point(0,-300),Point(0,300))              #for drawing Y-axis
Y.setArrow('both')
Y.setOutline('Black')
Y.draw(window)
msg=Text(Point(10,290), "+Y")                    
msg.draw(window)
msg=Text(Point(10,-290), "-Y")                    
msg.draw(window)

msg=Text(Point(0,0), "(0,0)")                     #for origin
msg.draw(window)


for i in range(1,4):
        x1=po[i-1][0]
        y1=po[i-1][1]
        x2=po[i][0]
        y2=po[i][1]
        draw_line(x1,y1,x2,y2,"Black")
x1=po[0][0]
y1=po[0][1]
x2=po[3][0]
y2=po[3][1]
draw_line(x1,y1,x2,y2,"Black")
msg =Text(Point(x_min,y_min),"("+str(x_min)+","+str(y_min)+")")  
msg.draw(window)
msg =Text(Point(x_max,y_max),"("+str(x_max)+","+str(y_max)+")")
msg.draw(window)
draw_line(a0,b0,a1,b1,"GREEN")
msg =Text(Point(a0,b0),"("+str(a0)+","+str(b0)+")")  
msg.draw(window)
msg =Text(Point(a1,b1),"("+str(a1)+","+str(b1)+")")
msg.draw(window)
parametricClip(a0,b0,a1,b1)


window.getMouse()
window.close()
