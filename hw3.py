import matplotlib.pyplot as plt
import numpy as np
from math import *

x1 = np.linspace(0,50,1000)

y1 = [cos(i/3.98) for i in x1]

y2 = [-cos(i/3.98) for i in x1]

y3 = [sin(i/3.98) for i in x1]

y4 = [-sin(i/3.98) for i in x1]

plt.plot(x1,y1,color = "red")
plt.plot(x1,y2,color = "blue")
plt.plot(x1,y3,color = "yellow")
plt.plot(x1,y4,color='green')

plt.show()

