import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure("HERMITE CURVE")
ax=fig.add_subplot(111,projection='3d')

P0=[0,0,0]
P1=[10,10,0]
D0=45
D1=45
D0=math.tan(math.pi/180*D0)
D1=math.tan(math.pi/180*D1)

T=np.array([[2,-2,1,1],[-3,3,-2,-1],[0,0,1,0],[1,0,0,0]])
AX=np.array([[P0[0]],[P1[0]],[D0],[D1]])
AY=np.array([[P0[1]],[P1[1]],[D0],[D1]])
AZ=np.array([[P0[2]],[P1[2]],[D0],[D1]])

p_x=P0[0]
p_y=P0[1]
p_z=P0[2]

for i in range(0,101):
    u=i/100
    U=np.array([[u*u*u,u*u,u,1]])
    x=U.dot(T.dot(AX))
    y=U.dot(T.dot(AY))
    z=U.dot(T.dot(AZ))
    x=x[0][0]
    y=y[0][0]
    z=z[0][0]
    ax.plot([p_x,x],[p_y,y],[p_z,z])
    p_x=x
    p_y=y
    p_z=z

plt.xlabel("X_axis")
plt.ylabel("Y_axis")





plt.show()
