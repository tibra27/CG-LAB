import numpy as np
import math
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

	
def Trans(q,tx,ty,tz,centerx,centery,centerz):
	shift=q.tolist()
	for i in range(len(shift)):
		shift[i][0]=shift[i][0]-centerx
		shift[i][1]=shift[i][1]-centery
		shift[i][2]=shift[i][2]-centerz
	q=np.array(shift)
	t=np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[tx,ty,tz,1]])
	tr=q.dot(t)
	l=tr.tolist()
	for i in range(len(l)):
		l[i][0]=l[i][0]+centerx
		l[i][1]=l[i][1]+centery
		l[i][2]=l[i][2]+centerz
	
	tr=np.array(l)
	return tr

def Scale(q,sx,sy,sz,centerx,centery,centerz):
	shift=q.tolist()
	for i in range(len(shift)):
		shift[i][0]=shift[i][0]-centerx
		shift[i][1]=shift[i][1]-centery
		shift[i][2]=shift[i][2]-centerz
	q=np.array(shift)
	s=np.array([[sx,0,0,0],[0,sy,0,0],[0,0,sz,0],[0,0,0,1]])
	sc=q.dot(s)
	l=sc.tolist()
	for i in range(len(l)):
		l[i][0]=l[i][0]+centerx
		l[i][1]=l[i][1]+centery
		l[i][2]=l[i][2]+centerz
	sc=np.array(l)
	return sc

def Rotate(q,theta,centerx,centery,centerz):
	shift=q.tolist()
	ch=int(input("enter 1-> x-axis 2-> y-axis 3-> z-axis "))
	
	for i in range(len(shift)):
		shift[i][0]=shift[i][0]-centerx
		shift[i][1]=shift[i][1]-centery
		shift[i][2]=shift[i][2]-centerz
	q=np.array(shift)
	if(ch == 3):
		s=np.array([[math.cos(theta),math.sin(theta),0,0],[(-1*math.sin(theta)),math.cos(theta),0,0],[0,0,1,0],[0,0,0,1]])
	elif(ch == 1):
		s=np.array([[1,0,0,0],[0,math.cos(theta),math.sin(theta),0],[0,(-1*math.sin(theta)),math.cos(theta),0],[0,0,0,1]])
	elif(ch == 2):
		s=np.array([[math.cos(theta),0,(-1*math.sin(theta)),0],[0,1,0,0],[(math.sin(theta)),0,math.cos(theta),0],[0,0,0,1]])
	else:
		print("wrong choice");
	sc=q.dot(s)
	l=sc.tolist()
	for i in range(len(l)):
		l[i][0]=l[i][0]+centerx
		l[i][1]=l[i][1]+centery
		l[i][2]=l[i][2]+centerz
	sc=np.array(l)
	return sc



def RotateAA(q,theta,centerx,centery,centerz,aax1,aay1,aaz1,A,B,C):
	V=math.sqrt((B*B+C*C))
	L=math.sqrt((A*A+B*B+C*C))
	shift=q.tolist()
	c=C/V
	s=B/V
	c1=A/L
	s1=V/L
	for i in range(len(shift)):
		shift[i][0]=shift[i][0]-centerx
		shift[i][1]=shift[i][1]-centery
		shift[i][2]=shift[i][2]-centerz
	q=np.array(shift)
	ss=np.array([[1,0,0,(-1*aax1)],[0,1,0,(-1*aay1)],[0,0,1,(-1*aaz1)],[0,0,0,1]]) #Translation to pass from origin
	sc=q.dot(ss)
	ss=np.array([[1,0,0,0],[0,c,s,0],[0,(-1*s),c,0],[0,0,0,1]]) #To bring in x-z plane
	sc=sc.dot(ss)
	ss=np.array([[s1,0,c1,0],[0,1,0,0],[(-1*c1),0,s1,0],[0,0,0,1]]) #To make it z-axis 
	sc=sc.dot(ss)
	ss=np.array([[math.cos(theta),math.sin(theta),0,0],[(-1*math.sin(theta)),math.cos(theta),0,0],[0,0,1,0],[0,0,0,1]])#Actual Rotation
	sc=sc.dot(ss)
	ss=np.array([[s1,0,(-1*c1),0],[0,1,0,0],[(c1),0,s1,0],[0,0,0,1]]) #Inverse of making it z-axis 
	sc=sc.dot(ss)
	ss=np.array([[1,0,0,0],[0,c,(-1*s),0],[0,(s),c,0],[0,0,0,1]]) #Inverse of bringing in x-z plane
	sc=sc.dot(ss)
	ss=np.array([[1,0,0,(aax1)],[0,1,0,(aay1)],[0,0,1,(aaz1)],[0,0,0,1]]) # Inverse of Translation
	sc=sc.dot(ss)
	l=sc.tolist()
	for i in range(len(l)):
		l[i][0]=l[i][0]+centerx
		l[i][1]=l[i][1]+centery
		l[i][2]=l[i][2]+centerz
	sc=np.array(l)
	n = len(polygon)
	for i in range(0,n-1):
		ax.plot([polygon[i][0], polygon[i+1][0]], [polygon[i][1], polygon[i+1][1]],[polygon[i][2], polygon[i+1][2]])
	ax.plot([polygon[n-1][0], polygon[0][0]], [polygon[n-1][1], polygon[0][1]],[polygon[n-1][2], polygon[0][2]])
	plt.show()
	return sc

polygon = [[0,0,0,1],[1,0,0,1],[1,0,1,1],[0,0,1,1],[0,0,0,1],[0,1,0,1],[1,1,0,1],[1,1,1,1],[0,1,1,1],[0,1,0,1],[1,1,0,1],[1,0,0,1],[1,0,1,1],[1,1,1,1],[0,1,1,1],[0,0,1,1]]
n2=8
for kj in range(0,0):
	x11=int(input("x"+str(kj+1)+" "));
	y11=int(input("y"+str(kj+1)+" "));
	z11=int(input("z"+str(kj+1)+" "));
	polygon.append([x11,y11,z11,1])
fig = plt.figure("INITIAL")
ax = fig.add_subplot(111, projection='3d')
n = len(polygon)
for i in range(0,n-1):
    ax.plot([polygon[i][0], polygon[i+1][0]], [polygon[i][1], polygon[i+1][1]],[polygon[i][2], polygon[i+1][2]])
ax.plot([polygon[n-1][0], polygon[0][0]], [polygon[n-1][1], polygon[0][1]],[polygon[n-1][2], polygon[0][2]])
plt.show()

xm=[]
ym=[]
zm=[]
for i in range(len(polygon)):
	xm.append(polygon[i][0])
	ym.append(polygon[i][1])
	zm.append(polygon[i][2])

centerx=sum(xm[:-1])/n2
centery=sum(ym[:-1])/n2
centerz=sum(zm[:-1])/n2

polyarr=np.array(polygon)
traask=int(input("enter 1 if want to do translation else 0"));
if(traask == 1):
        tx=int(input("enter tx "))
        ty=int(input("enter ty "))
        tz=int(input("enter tz "))
        polyarr=Trans(polyarr,tx,ty,tz,centerx,centery,centerz)
        polygon=polyarr.tolist()
        fig = plt.figure("AFTER TRANSLATION")
        ax = fig.add_subplot(111, projection='3d')
        n = len(polygon)
        for i in range(0,n-1):
                ax.plot([polygon[i][0], polygon[i+1][0]], [polygon[i][1], polygon[i+1][1]],[polygon[i][2], polygon[i+1][2]])
        ax.plot([polygon[n-1][0], polygon[0][0]], [polygon[n-1][1], polygon[0][1]],[polygon[n-1][2], polygon[0][2]])
        plt.show()

scaask=int(input("enter 1 if want to do scaling else 0"));
if(scaask == 1):
        sx=int(input("enter sx "))
        sy=int(input("enter sy "))
        sz=int(input("enter sz "))
        polyarr=Scale(polyarr,sx,sy,sz,centerx,centery,centerz)
        polygon=polyarr.tolist()
        fig = plt.figure("AFTER SCALING")
        ax = fig.add_subplot(111, projection='3d')
        n = len(polygon)
        for i in range(0,n-1):
                ax.plot([polygon[i][0], polygon[i+1][0]], [polygon[i][1], polygon[i+1][1]],[polygon[i][2], polygon[i+1][2]])
        ax.plot([polygon[n-1][0], polygon[0][0]], [polygon[n-1][1], polygon[0][1]],[polygon[n-1][2], polygon[0][2]])
        plt.show()


rotask=int(input("enter 1 if want to do rotation else 0"));
if(rotask == 1):
        theta=int(input("enter angle of rotation "))
        theta=(theta*math.pi)/180;
        polyarr=Rotate(polyarr,theta,centerx,centery,centerz)
        polygon=polyarr.tolist()
        fig = plt.figure("AFTER ROTATION")
        ax = fig.add_subplot(111, projection='3d')
        n = len(polygon)
        for i in range(0,n-1):
                ax.plot([polygon[i][0], polygon[i+1][0]], [polygon[i][1], polygon[i+1][1]],[polygon[i][2], polygon[i+1][2]])
        ax.plot([polygon[n-1][0], polygon[0][0]], [polygon[n-1][1], polygon[0][1]],[polygon[n-1][2], polygon[0][2]])
        plt.show()


rotaask=int(input("enter 1 if want to do rotation about arbitrary axis else 0"));
if(rotaask == 1):
	aax1=int(input("enter x1 of arbitray axis "))
	aay1=int(input("enter y1 of arbitray axis "))
	aaz1=int(input("enter z1 of arbitray axis "))
	A=int(input("enter x direction ratio "))
	B=int(input("enter y direction ratio "))
	C=int(input("enter z direction ratio "))
	theta=int(input("enter angle of rotation "))

	theta=(theta*math.pi)/180
	polyarr=RotateAA(polyarr,theta,centerx,centery,centerz,aax1,aay1,aaz1,A,B,C)
	polygon=polyarr.tolist()
	fig = plt.figure("AFTER ROTATION ABOUT AXIS PASSING THROUGH ("+str(aax1)+","+str(aay1)+","+str(aaz1)+") and dirction Ratios ("+str(A)+","+str(B)+","+str(C)+")")
	ax = fig.add_subplot(111, projection='3d')

	n = len(polygon)
	for i in range(0,n-1):
		ax.plot([polygon[i][0], polygon[i+1][0]], [polygon[i][1], polygon[i+1][1]],[polygon[i][2], polygon[i+1][2]])
	ax.plot([polygon[n-1][0], polygon[0][0]], [polygon[n-1][1], polygon[0][1]],[polygon[n-1][2], polygon[0][2]])
	plt.show()
