import matplotlib.pyplot as plt
import math
import numpy as np

g=9.81 #gravity acceleration constant
r=1 #radius for the object
delta=0.2

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(224)

maxY=int(input("Enter height: "))
ax1.set_xlim([0,r*10])
xPos=r*10/2
ax1.set_ylim([0-r,maxY+r]) # show complete object shape at its highest 
t=math.sqrt(2*maxY/g)


#below are plots for time-distance & time-velocity
x2=np.linspace(0,t, 100)
y2=0.5*g*x2*x2
ax2.set_ylabel('distance')
ax2.set_xlabel('time')

x3=np.linspace(0,t, 100)
y3=g*x3
ax3.set_ylabel('velocity')
ax3.set_xlabel('time')

ax2.plot(x2,y2)
ax3.plot(x3,y3)

#below is plot for falling ball 
ax1.set_aspect('equal')

yPos=[maxY]
curY=maxY;

i=t
while (i>=0):
    i=i-delta
    curY=maxY-(0.5*g*i*i)
    yPos.append(curY)
if (i != 0):
    yPos.append(r)

for j in yPos:
    circle=plt.Circle((xPos,j), r)
    ax1.add_patch(circle)



plt.show()
