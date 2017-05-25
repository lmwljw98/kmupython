import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(224)

x2 = np.linspace(0,10,100)
y2 = x2
ax2.set_ylabel('distance')
ax2.set_xlabel('time')

x3 = np.linspace(0,10,100)
y3=x3*x3
ax3.set_ylabel('velocity')
ax3.set_xlabel('time')

ax2.plot(x2,y2)
ax3.plot(x3,y3)

plt.show()
