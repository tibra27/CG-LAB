import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


f=plt.figure("2016UCP1103_BEZIRE_CURVE")
ax=f.add_subplot(111,projection='3d')

n=3
px=[10,20,20,30]
py=[10,30,30,10]
pz=[0,0,0,0]

qx=[-50,-50,0,10]
qy=[-10,-100,-10,10]
qz=[0,0,0,0]

def Comb(n,k):
    return(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))

for i in range(0,n):
    ax.plot([px[i],px[i+1]],[py[i],py[i+1]],[pz[i],pz[i+1]],"red")

p_x=px[0]
p_y=py[0]
p_z=pz[0]

for i in range(0,101):
    u=i/100
    x=0
    y=0
    z=0
    for k in range(0,n+1):
        blendfn=Comb(n,k)*math.pow(u,k)*math.pow(1-u,n-k)
        x+=px[k]*blendfn
        y+=py[k]*blendfn
        z+=pz[k]*blendfn
    ax.plot([p_x,x],[p_y,y],[p_z,z],"red")
    p_x=x
    p_y=y
    p_z=z

q_x=qx[0]
q_y=qy[0]
q_z=qz[0]
'''
for i in range(0,n):
    ax.plot([qx[i],qx[i+1]],[qy[i],qy[i+1]],[qz[i],qz[i+1]])
'''
for i in range(0,101):
    u=i/100
    x=0
    y=0
    z=0
    for k in range(0,n+1):
        blendfn=Comb(n,k)*math.pow(u,k)*math.pow(1-u,n-k)
        x+=qx[k]*blendfn
        y+=qy[k]*blendfn
        z+=qz[k]*blendfn
    ax.plot([q_x,x],[q_y,y],[q_z,z],"blue")
    q_x=x
    q_y=y
    q_z=z


plt.xlabel("X-AXIS")
plt.ylabel("Y-AXIS")
plt.show()
