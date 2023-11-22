import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([],[])
    return line

def animate(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    if i == FRAMES-1:
        plt.close()
    return line

FRAMES = 1000
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=FRAMES, interval=1, repeat=False)

plt.show()
