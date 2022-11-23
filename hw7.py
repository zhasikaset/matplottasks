import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(projection='3d')

x0 = np.array([np.random.randint(500,1500) for i in range(1000)])
y0 = np.array([np.random.randint(-500,1000) for i in range(1000)])
z0 = np.array([np.random.randint(-1000,0) for i in range(1000)])

x1 = np.array([np.random.randint(1000,2000) for i in range(1000)])
y1 = np.array([np.random.randint(0,1000) for i in range(1000)])
z1 = np.array([np.random.randint(-500,500) for i in range(1000)])

x2 = np.array([np.random.randint(1500,2500) for i in range(1000)])
y2 = np.array([np.random.randint(-500,500) for i in range(1000)])
z2 = np.array([np.random.randint(-500,0) for i in range(1000)])

ax.scatter(x0,y0,z0,color='blue')
ax.scatter(x1,y1,z1,color='red')
ax.scatter(x2,y2,z2,color='yellow')

plt.show()