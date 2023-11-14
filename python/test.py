import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line = ax.plot([], [], lw=2)

# def init():
#     line.set_data([],[])
#     return line

# def animate(i):
#     x = [1,2,3, 5]
#     y =  [1+i,2+i,3+i, 5+i]
#     line.set_data(x, y)
#     print(i, x, y)
#     if i == FRAMES-1:
#         plt.close()
#     return line

# FRAMES = 100
# anim = animation.FuncAnimation(fig, animate, init_func=init, frames=FRAMES, interval=30, repeat=False)

line.set_date([2,3], [6,7])

plt.show()
