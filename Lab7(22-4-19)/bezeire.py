import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure("BEZEIRE CURVE")
ax=fig.add_subplot(111,projection='3d')

N=4
n=N-1
px=[0,10,20,30]
py=[0,10,10,0]
pz=[0,0,0,0]

for i in range(0,n):
    ax.plot([px[i],px[i+1]],[py[i],py[i+1]],[pz[i],pz[i+1]])
def C(n,k):
    return(math.factorial(n)/(math.factorial(n-k)*math.factorial(k)))
p_x=px[0]
p_y=py[0]
p_z=pz[0]
x=0
y=0
z=0
for i in range(0,101):
    u=i/100
    x=0
    y=0
    z=0
    for k in range(0,n+1):
        blend=C(n,k)*math.pow(u,k)*math.pow(1-u,n-k)
        x+=(px[k]*blend)
        y+=(py[k]*blend)
        z+=(pz[k]*blend)
    ax.plot([p_x,x],[p_y,y],[p_z,z])
    p_x=x
    p_y=y
    p_z=z



plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()
