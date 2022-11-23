import numpy as np
import matplotlib.pyplot as plt
#fractal given by recursive formula z0 = 0,z(n+1)=z^2+c,if for this c our sequence will converge then this c is in our fractal 
xmin, xmax, ymin, ymax = -2.5, 1.5, -2, 2
nums = 250
max_iterations = 100
infinity_border = 100
points = np.zeros((nums, nums))
x = np.linspace(xmin, xmax, nums)
y = np.linspace(ymin, ymax, nums)
for i in range(len(x)):
    for j in range(len(x)):
        c = x[i] + 1j * y[j]
        z = 0+1j*0
        for k in range(max_iterations):
            z = z*z + c
            if abs(z) > infinity_border:
                points[i, j] = 1
                break
for i in range(len(points)):
    for j in range(len(points)):
        if points[i][j]==0:
            plt.scatter(i,j,s=3,color="red")
plt.show()