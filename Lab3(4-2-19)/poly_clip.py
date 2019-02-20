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


#functions for polygon clipping
def inside(point,clip_edge):
    if clip_edge[1][0]>clip_edge[0][0]:  # for bottom clipping edge
        if point[1]>=clip_edge[0][1]:
            return True
    if clip_edge[1][0]<clip_edge[0][0]:  # for top clipping edge
        if point[1]<=clip_edge[0][1]:
            return True
    if clip_edge[1][1]>clip_edge[0][1]:   # for right clipping edge
        if point[0]<=clip_edge[1][0]:
            return True
    if clip_edge[1][1]<clip_edge[0][1]: #for left clipping edge
        if point[0]>=clip_edge[1][0]:
            return True
    return False

def intersection(s,p,clip_edge):
    if clip_edge[0][1]==clip_edge[1][1]:  #clipping edge is horizontal
        y=clip_edge[0][1]
        x=s[0]+(y-s[1])*(p[0]-s[0])//(p[1]-s[1])
    else:                                 #clipping edge is vertical
        x=clip_edge[0][0]
        y=s[1]+(x-s[0])*(p[1]-s[1])//(p[0]-s[0])
    return [x,y]

                        
def clippolygon(input,in_len,clip_edge):
    output=[]
    s=input[in_len-1]
    for i in range(0,in_len):
        p=input[i]
        if inside(p,clip_edge):
            if inside(s,clip_edge):
                output.append(p)
            else:
                i=intersection(s,p,clip_edge)
                output.append(i)
                output.append(p)
        else:
            if inside(s,clip_edge):
                i=intersection(s,p,clip_edge)
                output.append(i)
        s=p
    return output



#taking input 
print("Enter diagonal points of rectangle:")
x_min=int(input("Enter x_min:"))
y_min=int(input("Enter y_min:"))
x_max=int(input("Enter x_max:"))
y_max=int(input("Enter y_max:"))
po=[]
po.append([x_min,y_min])
po.append([x_max,y_min])
po.append([x_max,y_max])
po.append([x_min,y_max])
print("Enter number of vertices in polygon:")
n=int(input())
poly=[]
for i in range(0,n):
    a0=int(input("Enter x coordinate:"))
    b0=int(input("Enter y coordinate:"))
    poly.append([a0,b0])

        
window=GraphWin("2016UCP1103_CLIPPING-3",600,600)           #for viewport(device coordinates)

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
        draw_line(x1,y1,x2,y2,"yellow")
x1=po[0][0]
y1=po[0][1]
x2=po[3][0]
y2=po[3][1]
draw_line(x1,y1,x2,y2,"yellow")
for i in range(0,n-1):
    x1=poly[i][0]
    y1=poly[i][1]
    x2=poly[i+1][0]
    y2=poly[i+1][1]
    draw_line(x1,y1,x2,y2,"Green")
x1=poly[n-1][0]
y1=poly[n-1][1]
x2=poly[0][0]
y2=poly[0][1]
draw_line(x1,y1,x2,y2,"Green")
msg =Text(Point(x_min,y_min),"("+str(x_min)+","+str(y_min)+")")  
msg.draw(window)
msg =Text(Point(x_max,y_max),"("+str(x_max)+","+str(y_max)+")")
msg.draw(window)

clip_edge1=[[x_min,y_min],[x_max,y_min]]
clip_edge2=[[x_max,y_min],[x_max,y_max]]
clip_edge3=[[x_max,y_max],[x_min,y_max]]
clip_edge4=[[x_min,y_max],[x_min,y_min]]
poly=clippolygon(poly,len(poly),clip_edge1)
poly=clippolygon(poly,len(poly),clip_edge2)
poly=clippolygon(poly,len(poly),clip_edge3)
poly=clippolygon(poly,len(poly),clip_edge4)
ver=len(poly)

for i  in range(0,ver-1):
    x1=poly[i][0]
    y1=poly[i][1]
    x2=poly[i+1][0]
    y2=poly[i+1][1]
    draw_line(x1,y1,x2,y2,"RED")
x1=poly[ver-1][0]
y1=poly[ver-1][1]
x2=poly[0][0]
y2=poly[0][1]
draw_line(x1,y1,x2,y2,"RED")
    


window.getMouse()
window.close()
