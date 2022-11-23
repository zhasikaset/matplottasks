import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,1000)
y = x*x

plt.plot(x,y)
plt.grid(True)
plt.show()