from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from math import *

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
t = np.linspace(-2,16,50)
x = [5*cos(i) for i in t]
y = [5*sin(i) for i in t]
z = [i for i in t]
ax.plot(x,y,z,zdir='z',label='zs=0, zdir=z',marker = 'o')
ax.view_init(30,45)
plt.show()
