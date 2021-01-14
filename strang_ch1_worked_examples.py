# 1.1A
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x_ax = list(range(-100, 101, 1))
y_ax = list(range(-100, 101, 1))
z_ax = list(range(-100, 101, 1))
empty_ax = [0]*len(x_ax)
flat_ax = [1]*len(x_ax)

vx, vy = np.meshgrid(x_ax, y_ax)
vz = vx*0 + vy*0

wy, wz = np.meshgrid(y_ax, z_ax)
wx = wy*0 + wz*0

# plot v
plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(vx, vy, vz, color='r')

# plot w
plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(wx, wy, wz, color='b')

# plot intersection of v and w
plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(vx, vy, vz, color='r', alpha=0.5)
plt3d.plot_surface(wx, wy, wz, color='b', alpha=0.5)

# add example points from description
sample_x = [0, 2, 5]
sample_y = [0, 3, 7]
sample_z = [0, 1, 2]
plt3d.scatter3D(sample_x, sample_y, sample_z, color='k')


plt.show()

'''
# 1.1B
import numpy as np
import matplotlib.pyplot as plt

xmin = -50
xmax = 50

# show all whole numbers
int_c = list(range(xmin, xmax, 1))
y = [0] * len(int_c)
plt.plot(int_c, y, 'o')
#plt.hlines(0, -10, 10, linestyle='dotted')#c[0], c[-1])

# show all positive numbers 
# i'm representing these as a line 
pos_c = list(range(0, xmax, 1))
y = [0] * len(pos_c)
plt.plot(pos_c, y, '-')

# entire c space
pos_int_c = [x for x in int_c if x >= 0]
y = [0] * len(pos_int_c)
plt.plot(pos_int_c, y)

# plotting d
for x in pos_int_c:
    plt.axvline(x)

plt.xlim(-10,10)
plt.show()
'''