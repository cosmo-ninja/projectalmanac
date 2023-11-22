import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = plt.axes(xlim=(0, 25), ylim=(-2, 2))
line1, line2, line3 = ax.plot([], [], [], [], [], [], lw=2)
# line2, = ax.plot([],[], lw=2)


def animate(i):
    x = np.arange(0, 0.1*i, 0.01)
    y = np.sin(x)
    z = np.cos(x)
    w = np.exp(x)
    if i == FRAMES-1:
        plt.close()
    return line1.set_data(x, y), line2.set_data(x, z), line3.set_data(x, w)

FRAMES = 250
anim = animation.FuncAnimation(fig, func=animate, frames=FRAMES, interval=20, repeat=False)

plt.show()
