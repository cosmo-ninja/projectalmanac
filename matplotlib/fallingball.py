import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D


g = 9.8
h = 200


t = np.sqrt((2*h)/9.8)
INTERVAL = 300
FR = int((t*1000)/INTERVAL)

th = np.linspace(0, t, FR)
ht = h - (0.5*g*(th*th))

fig = plt.figure()
ax = plt.axes(xlim=(0,5), ylim=(-5, 210))
line, = ax.plot([],[], marker='o')

def animate(frame):
    # print(frame)
    if frame == FR-1:
        plt.close()
    return line.set_data(2, ht[frame])

anim = animation.FuncAnimation(fig, animate, FR, interval=200)
# print(th)
# print(ht)

plt.show()