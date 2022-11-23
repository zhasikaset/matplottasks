import matplotlib.pyplot as plt
import numpy as np
import random

nums = np.random.randint(40,50)

sizes = np.array([(np.random.uniform(50,200)) for i in range(nums)])

x = np.array([round(np.random.uniform(-0.2,1.4), 4) for i in range(nums)])
y = np.array([round(np.random.uniform(-0.2,1.2), 4) for i in range(nums)])

for i in range(nums):
    plt.scatter(x[i],y[i],s = sizes[i],color = random.choice(["blue","red",'yellow']),alpha = 0.5)

plt.show()
