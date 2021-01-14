# 1.1A
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# this describes v and w
'''
xs = [0, 1, 100]
ys = [0, 1, 100]
zs = [0, 1, 100]
flat = [0, 0, 0]

plt3d = plt.figure().gca(projection='3d')
plt3d.plot(xs, ys, flat)
plt3d.plot(flat, ys, zs)
plt3d.legend()

plt.show()
'''

# this describes cv and dw

'''
c = list(range(0,6))
d = list(range(0,6))

v = [1,1,0]
w = [0,1,1]
test_xs = [2,5]
test_ys = [3,7]
test_zs = [1,2]
xs = []
ys = []
zs = []

for i in c:
    for j in d:
        xs.append(i)
        ys.append(i+j)
        zs.append(j)

for i in range(0, len(xs)):
    if xs[i] + zs[i]!= ys[i]:
        print(xs[i], ys[i], zs[i])

plt3d = plt.figure().gca(projection='3d')
plt3d.scatter3D(xs, ys, zs, color='k')
plt3d.scatter3D(test_xs, test_ys, test_zs, color='r')

plt.show()
'''

# this describes cv + dw
'''
cv = []
dw = []
for i in c:
    temp_cv = v*i
    cv.append([i,i,0])
    dw.append([0,i,i])

plane = []
xs = [2,5]
ys = [3,7]
zs = [1,2]
for i in range(0, len(cv)):
    x = cv[i][0] + dw[i][0]
    y = cv[i][1] + dw[i][1]
    z = cv[i][2] + dw[i][2]
    xs.append(x)
    ys.append(y)
    zs.append(z)
    plane.append([x,y,z])

plt3d = plt.figure().gca(projection='3d')
plt3d.scatter3D(xs, ys, zs, color='k')


plt.show()
'''


# https://observablehq.com/@harrystevens/adding-three-dimensional-vectors
'''
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

#1.1C