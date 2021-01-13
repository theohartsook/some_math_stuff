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