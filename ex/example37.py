import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(224)

maxY = 100
ax1.set_xlim([0,20])
ax1.set_ylim([0,maxY])

#x1 = range(0,100)
#y1 = [i/2 for i in x1]

x2 = range(0,10)
y2 = [i/2 for i in x2]

x3 = range(0,4)
y3 = [i/2 for i in x3]

ax2.plot(x2,y2)
ax3.plot(x3,y3)

vPos = 90
ax1.set_aspect('equal')

vPos = []
curY = maxY

while(curY >= 0):
    curY = curY - 10
    vPos.append(curY)

for j in vPos:
    circle = plt.Circle((10,j),1)
    ax1.add_patch(circle)

plt.show()
